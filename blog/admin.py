from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'created_at', 'updated_at',)

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)