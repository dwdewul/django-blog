from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdminModel(admin.ModelAdmin):
    list_display = ['title', 'updated_at', 'timestamp']
    list_display_links = ('updated_at',)
    list_editable = ('title',)
    list_filter = ('updated_at', 'title')

    class Meta:
        model = Post

admin.site.register(Post, PostAdminModel)
