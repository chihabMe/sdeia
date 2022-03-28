from django.urls import path 
from . import views
app_name = 'posts'

urlpatterns = [
    path('',views.home,name='home'),
    path("post/like-add", views.post_like, name="post_like"),
    path("post/comment-add", views.comment_add, name="post_comment"),
    path("post/comments-get", views.comments_get, name="post_comments_get"),
    
]
