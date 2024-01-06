from django.urls import path

from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('research', views.research, name='research'),
   path('about', views.about, name='about'),
   path('profile', views.profile, name='profile'),
   path('all_vol', views.all_vol, name='all_vol'),
   path('all_org', views.all_org, name='all_org'),
   path('view_profile/<int:user_id>', views.view_profile, name='view_profile')
]