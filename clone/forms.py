from django import forms
from .models import Profile,Image,Comments
from django.forms import ModelForm,Textarea

class NewImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['post_date','user','likes']

class UpdateProfile(forms.ModelForm):
     class Meta:
         model = Profile
         exclude =['userId']
class NewComment(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=['user','images']