from django.db import models
from django.conf import settings

from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils.timezone import get_fixed_timezone
from django.dispatch import receiver
from django.utils.safestring import mark_safe

from ckeditor_uploader.fields import RichTextUploadingField 


class Blog(models.Model):
    tagline = models.TextField()
    headline = models.CharField(max_length=255)
    body_text = RichTextUploadingField()
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)

    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.headline

    def get_markdown_description(self):
        data = self.body_text
        return mark_safe(data)


def populate_blog_slug(sender, instance, **kwargs):
    if not instance.slug:
        
        slug = slugify(instance.headline)
        instance.slug = slug

pre_save.connect(populate_blog_slug, sender=Blog)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
