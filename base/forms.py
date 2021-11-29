from django import forms
from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from base.models import Blog, Contact
from ckeditor_uploader.widgets import CKEditorUploadingWidget 


class BlogForm(forms.ModelForm):

    body_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = ['headline', 'tagline', 'body_text']


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']