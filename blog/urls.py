from django.urls import path


from . import views

urlpatterns = [
    path('', views.blog_index, name="blog_index"),
    path('<blog_slug>-&id=<blog_id>/', views.blog_detail, name="blog_detail"),
    path('<blog_slug>-&id=<blog_id>/edit/', views.edit_blog, name="edit_blog"),
    path('create/', views.create_blog, name="create_blog"),
]