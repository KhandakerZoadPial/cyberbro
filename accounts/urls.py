from django.urls import path

from . import views

urlpatterns = [
   path('login', views.login, name='login'),
   path('logout', views.user_logout, name='user_logout'),
   path('org_signup', views.org_signup, name='org_signup'),
   path('vol_signup', views.vol_signup, name='vol_signup')
]