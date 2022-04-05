from django.db import models
from posts.models import Post 
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class PostNotifications(models.Model):
    body = models.TextField(max_length=300)
    user = models.ForeignKey(User,related_name='user_notifications',on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    post  = models.ForeignKey(Post,related_name='post_notifications',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-date',)