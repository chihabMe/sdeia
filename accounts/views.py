from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import  Profile 
from django.http import JsonResponse
# Create your views here.

def like_add(request):
    if request.method=='POST':
        data = {}
        post_id = request.POST.get('postId')
        print('----------')
        print(post_id)
        print('----------')
        data['msg']='success'
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