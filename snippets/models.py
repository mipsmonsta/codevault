from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#007bff')  # Hex color code
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('snippets:tag_detail', kwargs={'pk': self.pk})


class Snippet(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('cpp', 'C++'),
        ('csharp', 'C#'),
        ('php', 'PHP'),
        ('ruby', 'Ruby'),
        ('go', 'Go'),
        ('rust', 'Rust'),
        ('swift', 'Swift'),
        ('kotlin', 'Kotlin'),
        ('typescript', 'TypeScript'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('sql', 'SQL'),
        ('bash', 'Bash'),
        ('powershell', 'PowerShell'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    code = models.TextField()
    notes = models.TextField(blank=True, help_text="Add your remarks and notes about this code snippet")
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default='python')
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('snippets:snippet_detail', kwargs={'pk': self.pk})
    
    def get_markdown_export(self):
        """Generate markdown content for export"""
        markdown = f"# {self.title}\n\n"
        markdown += f"**Language:** {self.get_language_display()}\n\n"
        
        if self.tags.exists():
            markdown += f"**Tags:** {', '.join([tag.name for tag in self.tags.all()])}\n\n"
        
        markdown += f"**Created:** {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        markdown += f"**Updated:** {self.updated_at.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        if self.notes:
            markdown += f"## Notes\n\n{self.notes}\n\n"
        
        markdown += f"## Code\n\n```{self.language}\n{self.code}\n```\n"
        
        return markdown
