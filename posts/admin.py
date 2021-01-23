from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author",)
    search_fields = ("text",)
    list_filter = ("pub_date",)
    '''Данное свойство сработает для всех пустых колонок:'''
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)


class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("pk", "title", "description", "slug",)
    search_fields = ("title", "description",)
    list_filter = ("title",)
    empty_value_display = "-пусто-"


admin.site.register(Group, GroupAdmin)