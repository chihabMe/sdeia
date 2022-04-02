
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
# Create your models here.
def namer(instance,filename):
    name = instance.user.username+"/"+filename
    print(name)
    return name
class Post(models.Model):
    body = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=namer,null=True,blank=True)
    slug = models.SlugField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_posts')
    likes = models.ManyToManyField(User,related_name='user_posts_likes',blank=True)
    public = models.BooleanField(default=True)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def get_likes_count(self):
        return self.likes.all().count()
    def get_comments_count(self):
        return self.post_comments.all().count()
    def get_post_time(self):
        res = timezone.now()-self.published
        res = res.total_seconds()
        if res<60 :
            res = str(int(res))+" s"
        elif res >=60 and res <60*60:
            res = str(int(res/60))+" min"
        elif res <60*60*24:
            res = str(int(res/(60*60)))+" h"
        else:
            res =str(int(res/(60*60*24)))+" days"
        return res
    def save(self,*args, **kwargs):
        if not self.slug :
            if self.body:
                self.slug = slugify(self.body[0:30])
            else:
                self.slug = slugify(self.image.name.split('.')[0])

        super(Post,self).save(*args, **kwargs)
        if self.image:
            image = Image.open(self.image.path)
            if image.width > 650 or image.height>400:
                output_size = (650,560)
                image.thumbnail(output_size)
                image.save(self.image.path)
    def __str__(self):
        return self.body[0:20]
    
    def get_absolute_url(self):
        pass 
    class Meta:
        ordering = ('-published','-updated')

class Comment(models.Model):
    body = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_comments')
    likes = models.ManyToManyField(User,related_name='user_comments_likes')
    post  = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_comments')
    def get_likes_count(self):
        return self.likes.all().count()
    def __str__(self):
        return self.body[0:20]
    