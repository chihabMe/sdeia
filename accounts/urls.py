from django.urls import path 
from . import views
app_name = 'accounts'

urlpatterns = [
    path('<str:username>/profile',views.profile_page,name='profile')
]