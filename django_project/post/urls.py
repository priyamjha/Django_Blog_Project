from django.urls import path
from . import views

urlpatterns = [
    path('create-post/', views.create_post, name='create-post'),
    path('post-details/<int:pk>/', views.post_details, name='post-details'),
    path('update-post/<int:pk>/', views.update_post, name='update-post'),
    path('delete-post/<int:pk>/', views.delete_post, name='delete-post'),
    path('all-created-posts/', views.all_created_posts, name='all-created-posts'),
    path('', views.all_posts, name='home'),
]
