from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
  path('',views.index,name='index'),
  path('',views.profile,name='profile'),
  path('',views.timeline,name='timeline'),
  path('pic/(\d+)',views.single_pic,name ='single_pic'),
  path('comment/(<id>\d+)',views.comment, name='comment'),
  path('profile/', views.profile, name='profile'),
  path('single_pic/(\d+)', views.single_pic, name='single_pic'),
  path('send/', views.send, name='send'),
  path('search_results/', views.search_results, name='search_results'),
  path('upload/profile', views.upload_profile, name='upload_profile'),
  path('accounts/login',views.login, name='login'),
  path('logout/',views.logout, name="logout"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)