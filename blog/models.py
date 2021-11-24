from django.db import models
from django.core.signals import request_finished
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils.timezone import get_fixed_timezone
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField 


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    content = RichTextUploadingField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_markdown_description(self):
        data = self.content
        return mark_safe(data)

def populate_blog_slug(sender, instance, **kwargs):
    if not instance.slug:
        
        slug = slugify(instance.title)
        instance.slug = slug

pre_save.connect(populate_blog_slug, sender=Blog)


