from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group', 'active')
    empty_value_display = '-пусто-'
    search_fields = ('text',)
    list_filter = ('pub_date',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'active')
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title",)}