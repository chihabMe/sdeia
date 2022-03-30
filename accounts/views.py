from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import  Profile 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


from .forms import LoginForm,SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.
def logout_page(request):
    logout(request)
    return redirect(reverse('accounts:login'))
def signup_page(request):
    form = SignUpForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            user = form.save(commit=False)
            print(user.username)
            user.save()
            return redirect(reverse('accounts:login'))
        
    context={
        'form':form
        }
    return render(request, 'accounts/signup.html',context)
def login_page(request):
    form = LoginForm(request.POST or None )
    errors=False 
    if request.method=='POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(reverse("posts:home"))
            errors=True
    context = {
        'form':form,
        'errors':errors
    }
    return render(request, 'accounts/login.html',context )
@login_required
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
@login_required
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
@login_required
def profile_page(request,username):
    user = get_object_or_404(User,username=username)
    profile = Profile.objects.get(user=user)
    context = {
        'user':user,
        'profile':profile,
        'page':'profile'

    }
    return render(request, 'accounts/profile.html',context)