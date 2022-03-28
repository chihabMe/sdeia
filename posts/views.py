from django.shortcuts import render
from .models import Post,Comment
from django.http import JsonResponse
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from django.core import serializers

import json
# Create your views here.
def comments_get(request):
    if request.method=='POST':
        data = {}
        post_id = request.POST.get('postId')
        post = get_object_or_404(Post,id=post_id)
        comments = post.post_comments.all()
        #comments_list = serializers.serialize('json', comments)
        #data['comments']=json.loads(comments_list)
        list_of_comments = []
        for comment in comments :
            res_com = {}
            res_com['username']=comment.user.username
            res_com['user_image']=comment.user.user_profile.image.url
            res_com['likes'] = comment.get_likes_count()
            res_com['body'] = comment.body
            list_of_comments.append(res_com)

        data['image']=post.image.url
        data['comments']=list_of_comments
        return JsonResponse(data)
        
def comment_add(request):
    if request.method=='POST':
        data = {}
        post_id = request.POST.get('postId')
        body = request.POST.get('body')
        post = get_object_or_404(Post,id=post_id)
        comment = Comment(user=request.user,body=body)
        comment.post=post 
        comment.save()
        print('--------------')
        print(post.get_comments_count())

        print('--------------')
        data['count']=post.get_comments_count()
        data['msg']='success'
        return JsonResponse(data)

def post_like(request):
    if request.method=='POST':
        data = {}
        post_id = request.POST.get('postId')
        post = get_object_or_404(Post,id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            data['operation']='dislike'
        else:
            post.likes.add(request.user)
            data['operation']='like'
        data['count']=post.get_likes_count()
        data['msg']='success'
        return JsonResponse(data)
def home(request):
    posts = Post.objects.all()
    context  ={
        'posts':posts,
        'page':'home'
    }
    return render(request,'posts/home.html',context)