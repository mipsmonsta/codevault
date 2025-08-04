from django import forms
from .models import Snippet, Tag


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'notes', 'language', 'tags', 'is_public']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter snippet title'
            }),
            'code': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 15,
                'placeholder': 'Enter your code here...',
                'style': 'font-family: monospace;'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Add your remarks and notes about this code snippet...'
            }),
            'language': forms.Select(attrs={
                'class': 'form-control'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'is_public': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        help_texts = {
            'code': 'Enter your code snippet here',
            'notes': 'Add any remarks, explanations, or notes about this code',
            'tags': 'Select or create tags to categorize this snippet',
            'is_public': 'Make this snippet visible to all users'
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'color']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tag name'
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'color',
                'title': 'Choose a color for this tag'
            })
        }
        help_texts = {
            'name': 'Enter a descriptive name for the tag',
            'color': 'Choose a color to visually distinguish this tag'
        } 