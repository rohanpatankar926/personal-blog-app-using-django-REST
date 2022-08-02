from re import S
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm,PasswordChangeForm
from blog_application.models import Profile

class SignupForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields={"username","first_name","last_name","email","password1","password2"}


    def __init__(self,*args,**kwargs):
        super(SignupForm,self).__init__(*args,**kwargs)
        self.fields["username"].widget.attrs["class"]="form-control"
        self.fields["password1"].widget.attrs["class"]="form-control"
        self.fields["password2"].widget.attrs["class"]="form-control"

class EditProfileForm(UserChangeForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_staff=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_active=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields={"username","first_name","last_name","email","password","last_login","is_superuser","is_staff","is_active"}

class PasswordChangeForm_(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',"type":"password"}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',"type":"password"}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',"type":"password"}))
    
    class Meta:
        model=User
        fields={"old_password","new_password1","new_password2"}

class ProfilePage(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('bio','profile_pic','Facebook','Instagram','Twitter','Personal_website','discord','LinkedIn')
        widgets={
        "bio":forms.Textarea(attrs={"class":"form-control"}),
        # "profile_pic":forms.ImageField(),
        "Facebook":forms.TextInput(attrs={"class":"form-control"}),
        "Instagram":forms.TextInput(attrs={"class":"form-control"}),
        "Twitter":forms.TextInput(attrs={"class":"form-control"}),
        "Personal_website":forms.TextInput(attrs={"class":"form-control"}),
        "discord":forms.TextInput(attrs={"class":"form-control"}),
        "LinkedIn":forms.TextInput(attrs={"class":"form-control"}), 
        }
