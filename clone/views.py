from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
# from .models import Image, Profile,Comments,Likes
# from .forms import NewComment,NewImage,UpdateProfile
from django.contrib.auth.models import User
from django.http import Http404,HttpResponse,HttpResponseRedirect

@login_required(login_url='/accounts/login')
def homepage (request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comments.objects.all()
    likes = Likes.objects.all()
    profile = Profile.objects.all()
    print(likes)
    return render(request,'home.html',locals())

@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfile(request.POST,request.FILES)
        if form.is_valid():
             profile = form.save(commit=False)
             profile.user = current_user
             profile.save()
        else:
            form=UpdateProfile()
    return render(request, 'profile/new.html',locals())
