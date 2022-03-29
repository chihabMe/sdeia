from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import  Profile 
from django.http import JsonResponse
# Create your views here.
def user_follow(request):
    data  = {}
    if request.method=='POST':
        username = request.POST.get('username')
        user  = get_object_or_404(User,username=username)
        if request.user in user.user_profile.followers.all():
            user.user_profile.followers.remove(request.user)
            request.user.user_profile.follwing.remove(user)
            data['operation']='unfollow'
        else:
            user.user_profile.followers.add(request.user)
            request.user.user_profile.follwing.add(user)
            data['operation']='follow'
        data['count']=user.user_profile.get_followers_count()
    return JsonResponse(data)
def user_search(request):
    data = {}
    if request.method=='POST':
        username  = request.POST.get('q')
        users = User.objects.filter(username__icontains=username)
    users_list=[]
    for user in users:
        user_dic={}
        user_dic['username']=user.username
        user_dic['image']=user.user_profile.image.url
        user_dic['profile']=user.user_profile.get_absolute_url()
        users_list.append(user_dic)
    data['results']=users_list
    return JsonResponse(data)
def profile_page(request,username):
    user = get_object_or_404(User,username=username)
    profile = Profile.objects.get(user=user)
    context = {
        'user':user,
        'profile':profile,
        'page':'profile'

    }
    return render(request, 'accounts/profile.html',context)