from django.contrib import admin
from .models import Snippet, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'author', 'created_at', 'updated_at', 'is_public']
    list_filter = ['language', 'is_public', 'created_at', 'tags']
    search_fields = ['title', 'code', 'notes', 'author__username']
    readonly_fields = ['created_at', 'updated_at']
    filter_horizontal = ['tags']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'language', 'author', 'is_public')
        }),
        ('Content', {
            'fields': ('code', 'notes')
        }),
        ('Tags', {
            'fields': ('tags',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
