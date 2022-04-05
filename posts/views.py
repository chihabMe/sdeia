from django.shortcuts import render

import notifications
from .models import Post,Comment
from django.http import JsonResponse
from notifications.models import PostNotifications 
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
@login_required
def post_add(request):
    data={}
    if request.method=='POST':
        body = request.POST.get('body')
        tags=[]
        if body:
            body_words_list = body.split(' ')
            for word in body_words_list:
                if '#' in word:
                    tags.append(word)
            print('---------------------')
            print(tags)
            print('---------------------')

        image = request.FILES.get('image')
        if  image :
            if image.content_type=='image/png' or  image.content_type=='image/jpeg' or  image.content_type=='image/jpg':
                pass    
            else :  
                image=None
        post = Post(user=request.user)
        if body:
            post.body=body 
        if image:
            post.image  = image
        post.save()
        data['body']=post.body 
        if post.image:
            data['image']=post.image.url

        else:
            data['image']=None
        data['user']=post.user.username
        data['user_image']=post.user.user_profile.image.url
        data['likes']=0
        data['comments']=0
        data['time']=post.get_post_time()
        data['published']=post.published
        return JsonResponse(data)
@login_required
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
@login_required
def comment_add(request):
    if request.method=='POST':
        data = {}
        post_id = request.POST.get('postId')
        body = request.POST.get('body')
        post = get_object_or_404(Post,id=post_id)
        comment = Comment(user=request.user,body=body)
        comment.post=post 
        comment.save()
        if request.user != post.user:
            body = f'{request.user.username} commented on your post '

            notifications = PostNotifications(user=post.user,body=body,post=post)
            notifications.save()
        data['count']=post.get_comments_count()
        data['msg']='success'
        return JsonResponse(data)
@login_required
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
        if post.user != request.user:
            body = f'{request.user.username} liked your post '
            notification = PostNotifications(user=post.user,post=post,body=body)
            notification.save()
        return JsonResponse(data)
@login_required
def home(request):

    posts = Post.objects.all()
    page = request.GET.get('p',1)
    
    paginator = Paginator(posts,10)
    try :
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts.page(1)
    except EmptyPage :
        posts = paginator.page(paginator.num_pages)
    notifications = PostNotifications.objects.filter(user=request.user,seen=False)
    if not notifications.exists():
        notifications=None
    context  ={
        'posts':posts,
        'page':'home',
        'notifications':notifications
    
    }
    return render(request,'posts/home.html',context)