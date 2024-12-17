"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('blogs/', views.blogs, name='blogs'),
    # Detail page for a single topic.
    path('blogs/<int:topic_id>/', views.blog, name='blog'),
    # Page for adding a new topic.
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page for adding a new entry.
    path('new_blog_post/<int:topic_id>/', views.new_blog_post, name='new_blog_post'),
    # Page for editing an entry.
    path('edit_blog_post/<int:entry_id>/', views.edit_blog_post, name='edit_blog_post'),
]