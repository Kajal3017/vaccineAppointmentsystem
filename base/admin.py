from django.contrib import admin
from base.models import Blog, Contact


class NotesAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'created_at', 'updated_at',)

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog)
admin.site.register(Contact)
