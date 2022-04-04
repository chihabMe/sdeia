from . import views
from django.urls import path


app_name = 'posts'


urlpatterns = [
    path('',views.home,name='home'),
    path("post/like-add", views.post_like, name="post_like"),
    path("post/comment-add", views.comment_add, name="post_comment"),
    path("post/comments-get", views.comments_get, name="post_comments_get"),
    path("post/post-add", views.post_add, name="post_add"),
    ]