from django.contrib import admin
from .models import Post, Group, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'group', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = 'empty_value'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Follow)
