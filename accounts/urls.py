from django.urls import path 
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView
from .token import TokenGenerator as generator
app_name = 'accounts'




urlpatterns = [
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('<str:username>/profile/',views.profile_page,name='profile'),
    path('profile/settings/',views.profile_settings,name='settings'),
    path('profile/password/settings/',views.password_settings,name='password_setting'),

    path('signup/',views.signup_page,name='signup'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.user_activate,name='activate'),
    path('search',views.user_search,name='user_search'),
    path('follow',views.user_follow,name='follow'),
    ##password reset 
    path('password/reset/',PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done'),template_name='registration/password_reset.html'),name='password_reset'),
    path('password/reset/done/',PasswordResetDoneView.as_view(template_name='registration/reset_done.html'),name='password_reset_done'),
    path('password/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='registration/password_reset/form.html'),name='password_reset_confirm'),
    path('password/reset/complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html.html'),name='password_reset_complete')
]