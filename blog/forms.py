from django import forms
from blog.models import Blog

from ckeditor_uploader.widgets import CKEditorUploadingWidget 
    

class BlogForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = ['title', 'content']