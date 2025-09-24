from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Snippet, Tag
from .forms import SnippetForm, TagForm


class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/snippet_list.html'
    context_object_name = 'snippets'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Snippet.objects.filter(is_public=True)
        
        # Search functionality
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(code__icontains=search_query) |
                Q(notes__icontains=search_query) |
                Q(tags__name__icontains=search_query)
            ).distinct()
        
        # Language filter
        language = self.request.GET.get('language', '')
        if language:
            queryset = queryset.filter(language=language)
        
        # Tag filter
        tag_id = self.request.GET.get('tag', '')
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['languages'] = Snippet.LANGUAGE_CHOICES
        context['tags'] = Tag.objects.all()
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_language'] = self.request.GET.get('language', '')
        context['selected_tag'] = self.request.GET.get('tag', '')
        return context


class UserSnippetListView(LoginRequiredMixin, ListView):
    model = Snippet
    template_name = 'snippets/user_snippets.html'
    context_object_name = 'snippets'
    paginate_by = 12
    
    def get_queryset(self):
        return Snippet.objects.filter(author=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['languages'] = Snippet.LANGUAGE_CHOICES
        context['tags'] = Tag.objects.all()
        return context


class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/snippet_detail.html'
    context_object_name = 'snippet'
    
    def get_queryset(self):
        # Allow viewing public snippets, and if authenticated, also user's own snippets
        if self.request.user.is_authenticated:
            return Snippet.objects.filter(
                Q(is_public=True) | Q(author=self.request.user)
            )
        return Snippet.objects.filter(is_public=True)


class SnippetCreateView(LoginRequiredMixin, CreateView):
    model = Snippet
    form_class = SnippetForm
    template_name = 'snippets/snippet_form.html'
    success_url = reverse_lazy('snippets:snippet_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Snippet created successfully!')
        return super().form_valid(form)


class SnippetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Snippet
    form_class = SnippetForm
    template_name = 'snippets/snippet_form.html'
    
    def test_func(self):
        snippet = self.get_object()
        return snippet.author == self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Snippet updated successfully!')
        return super().form_valid(form)


class SnippetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Snippet
    template_name = 'snippets/snippet_confirm_delete.html'
    success_url = reverse_lazy('snippets:snippet_list')
    
    def test_func(self):
        snippet = self.get_object()
        return snippet.author == self.request.user
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Snippet deleted successfully!')
        return super().delete(request, *args, **kwargs)


class TagDetailView(ListView):
    model = Snippet
    template_name = 'snippets/tag_detail.html'
    context_object_name = 'snippets'
    paginate_by = 12
    
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return Snippet.objects.filter(tags=self.tag, is_public=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


@login_required
def export_markdown(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    
    # Check if user can view this snippet
    if not snippet.is_public and snippet.author != request.user:
        messages.error(request, 'You do not have permission to export this snippet.')
        return redirect('snippets:snippet_list')
    
    markdown_content = snippet.get_markdown_export()
    
    response = HttpResponse(markdown_content, content_type='text/markdown')
    response['Content-Disposition'] = f'attachment; filename="{snippet.title.replace(" ", "_")}.md"'
    return response


def search_snippets(request):
    query = request.GET.get('q', '')
    if query:
        snippets = Snippet.objects.filter(
            Q(title__icontains=query) |
            Q(code__icontains=query) |
            Q(notes__icontains=query) |
            Q(tags__name__icontains=query),
            is_public=True
        ).distinct()
    else:
        snippets = Snippet.objects.filter(is_public=True)
    
    paginator = Paginator(snippets, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'snippets/search_results.html', {
        'snippets': page_obj,
        'query': query,
        'languages': Snippet.LANGUAGE_CHOICES,
        'tags': Tag.objects.all(),
    })


def tag_list(request):
    tags = Tag.objects.annotate(
        snippet_count=Count('snippet')
    ).order_by('name')
    return render(request, 'snippets/tag_list.html', {'tags': tags})


def tag_cloud(request):
    tags = Tag.objects.annotate(
        snippet_count=Count('snippet')
    )
    data = [
        {"name":tag.name, 
        "count":tag.snippet_count, 
        "id":str(tag.id),
        "color":tag.color} 
            for tag in tags]
    return render(request, 'snippets/tag_cloud.html', {'data': data})

class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'snippets/tag_form.html'
    success_url = reverse_lazy('snippets:tag_list')
    
    def form_valid(self, form):
        tag = form.save()
        
        # Check if this is an AJAX request
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'tag': {
                    'id': str(tag.id),
                    'name': tag.name,
                    'color': tag.color
                }
            })
        
        messages.success(self.request, 'Tag created successfully!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Check if this is an AJAX request
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'error': 'Invalid form data',
                'errors': form.errors
            })
        
        return super().form_invalid(form)
