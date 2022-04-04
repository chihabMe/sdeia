from enum import unique
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from PIL import Image 
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password,**extra_fields):
        if not username:
            raise ValueError('the username must be set ')
        if not email:
            raise ValueError("the email must be set ")
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,**extra_fields)
        user.set_password(password)
        user.save()
        return user 
    def create_superuser(self,email,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username,email,password, **extra_fields)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email =models.EmailField(max_length=299,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']
    
    objects = CustomUserManager()
    def __str__(self) :
        return self.username








def namer(instance , filename):
    return instance.username+"/profile/"+filename
class Profile(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(default='images/default.png',upload_to=namer,blank=True)
    user = models.OneToOneField(CustomUser, related_name='user_profile',on_delete=models.CASCADE)
    bio = models.TextField(max_length=400,null=True,blank=True)
    website = models.URLField(null=True,blank=True)


    followers = models.ManyToManyField(CustomUser,related_name='user_followers',blank=True)
    follwing = models.ManyToManyField(CustomUser,related_name='user_follwing',blank=True)
    likes = models.ManyToManyField(CustomUser,related_name='user_likes',blank=True)
    blocked_users = models.ManyToManyField(CustomUser,related_name='user_blocked',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"username": self.username})
    def get_likes_count(self):
        return self.likes.all().count()
    def get_posts_count(self):
        return self.user.user_posts.all().count()
    def get_followers_count(self):
        return self.followers.all().count()
    def get_following_count(self):
        return self.follwing.all().count()
    def save(self,*args, **kwargs):
        super(Profile,self).save(*args, **kwargs)
        if self.image:
            image = Image.open(self.image.path)
            if image.width>50 or image.height>50:
                output_size = (100,100)
                image.thumbnail(output_size)
                image.save(self.image.path)
    def __str__(self):
        return self.username
    
        

    
@receiver(post_save, sender=CustomUser)
def create_a_profile(sender,created,instance,**kwargs):
    if created:
        profile = Profile(user=instance,username=instance.username)

        profile.save()
