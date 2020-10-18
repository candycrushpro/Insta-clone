from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
  path('',views.homepage,name='homePage'),
  path('post/',views.post,name='post'),
  path('profile/',views.profile,name='profile'),
  path('user/(?P<username>\w+)',views.showprofile,name ='showprofile'),
  path('search/',views.search, name='search'),
  path('comment/(?P<image_id>\d+)', views.comment, name='comment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)