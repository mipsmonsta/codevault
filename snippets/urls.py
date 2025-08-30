from django.urls import path
from . import views

app_name = 'snippets'

urlpatterns = [
    # Main views
    path('', views.SnippetListView.as_view(), name='snippet_list'),
    path('my-snippets/', views.UserSnippetListView.as_view(), name='user_snippets'),
    path('search/', views.search_snippets, name='search'),
    
    # Snippet CRUD
    path('create/', views.SnippetCreateView.as_view(), name='snippet_create'),
    path('<int:pk>/', views.SnippetDetailView.as_view(), name='snippet_detail'),
    path('<int:pk>/edit/', views.SnippetUpdateView.as_view(), name='snippet_update'),
    path('<int:pk>/delete/', views.SnippetDeleteView.as_view(), name='snippet_delete'),
    path('<int:pk>/export/', views.export_markdown, name='export_markdown'),
    
    # Tag views
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),

    # Tags cloud views
    path('tags/cloud/', views.tag_cloud, name='tag_cloud'),
] 