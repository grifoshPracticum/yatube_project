from django.contrib import admin
from posts.models import Post, Group


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'pub_date', 'author', 'group')
    empty_value_display = '-пусто-'
    search_fields = ('text',)
    list_filter = ('pub_date',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'active')
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title",)}

# admin.site.register(Post)
