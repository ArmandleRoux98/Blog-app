from django.urls import path
from .views import create_blog, view_blog, edit_blog, home

app_name = 'blog_app'

urlpatterns = [
    path('create/', create_blog, name='create_blog'),
    path('view/<int:blog_id>', view_blog, name="view_blog"),
    path('edit/<int:blog_id>', edit_blog, name="edit_blog"),
    path('', home, name='home'),
]