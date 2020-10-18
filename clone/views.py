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
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImage(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homePage')
    else:
        form = NewImage()
    return render(request, 'post.html',locals())    

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

@login_required(login_url='/accounts/login')
def showprofile(request,username):
     profile = User.objects.get(username=username)
     print(profile)
     try:
        profile_details = Profile.get_by_id(profile.id)
        print(profile_details)
     except:
        profile_details = Profile.filter_by_id(profile.id)
        print(profile_details)
     images = Image.profile_images(profile.id)
     print(images)
     return render(request, 'profile/profile.html', {'profile':profile, 'profile_details':profile_details, 'images':images})    

def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        print(results)

        return render(request,'search.html',locals())
    return redirect('homePage')