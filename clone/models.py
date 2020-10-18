from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


class Profile(models.Model):
    profile_photo= models.ImageField(upload_to='profile',blank=True)
    bio=models.CharField(max_length=30)
    user= models.OneToOneField(User,blank=True, on_delete=models.CASCADE, related_name="profile")


    def __str__(self):
        return self.bio


    def save_profile(self):
        self.save()

    def delete_profile(self):
        profile=Profile.objects.all().delete()
        return profile
    
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(owner=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    @classmethod
    def get_profile_by_username(cls, owner):
        profiles = cls.objects.filter(owner__contains=owner)
        return profiles
class Image(models.Model):
      image = models.ImageField(upload_to='images/')
      name = models.CharField(max_length =30)
      image_caption = HTMLField()
      post_date = models.DateTimeField(auto_now_add=True)
      user = models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
      profile_details=models.ForeignKey(Profile,on_delete=models.CASCADE)
      

      def __str__(self):
          return self.name
      
      class Meta:
          ordering =['-post_date']
      
      def save_image(self):
          self.save()

      def delete_image(self):
          self.delete()

      @classmethod
      def all_images(cls):
          images = cls.objects.all()
          return images
      @classmethod
      def search_by_users(cls,term):
          result=cls.objects.filter(user__username__icontains=term)
          return result
    
      @classmethod
      def profile_images(cls, profile):
          images = Image.objects.filter(image__pk = User)
          return images


class Comments(models.Model):
    comment=models.TextField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ForeignKey(Image,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
    
    def save_comments(self):
        self.save()

    
    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls, id):
        comments = Comment.objects.filter(image__pk=id)
        return comments