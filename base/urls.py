from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/blog/', views.create_blog, name='create_blog'),
    path('contact_us/', views.create_contact_us, name='contact_us'),
    path('posts/', views.all_posts, name='all_posts'),
    path('projects/', views.projects, name='my_porjects'),
    path('skills/', views.skills, name='skills'),
]