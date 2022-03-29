from django.urls import path 
from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_page,name='login'),
    path('<str:username>/profile',views.profile_page,name='profile'),
    path('search',views.user_search,name='user_search'),
    path('follow',views.user_follow,name='follow')
]