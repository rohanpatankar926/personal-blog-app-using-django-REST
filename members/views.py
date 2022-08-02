
from django.shortcuts import render,get_object_or_404
from django.views import generic
import django
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm,UserCreationForm
from django.urls import reverse_lazy
from .forms import EditProfileForm, PasswordChangeForm_, ProfilePage, SignupForm
from django.contrib.auth.views import PasswordChangeView
from blog_application.models import Profile
# Create your views here.
class UserRegister(generic.CreateView):
    form_class=SignupForm
    template_name="registration/register.html"
    success_url=reverse_lazy("login")

class EditProfilePageView(generic.UpdateView):
    model=Profile
    template_name="regitrations/edit_profile_page.html"
    fields=['bio','profile_pic','Facebook','Instagram','Twitter','Personal_website','discord','LinkedIn']
    success_url=reverse_lazy("home")

class CreateProfilePageView(django.views.generic.edit.CreateView):
    model=Profile
    template_name="registration/create_user_profile.html"
    form_class=ProfilePage
    # fields="__all__"    
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class ShowProfilePageView(generic.DetailView):
    model=Profile
    template_name="registration/user_profile.html"
    def get_context_data(self,*args,**kwargs):
        # users=Profile.objects.all()
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        context=super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        context["page_user"]=page_user
        return context

class UserEdit(generic.UpdateView):
    form_class=EditProfileForm

    template_name="registration/edit_profile.html"
    success_url=reverse_lazy("home")

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangeForm_
    success_url=reverse_lazy("passwordsuccess")

def password_success(request):
    return render(request,"registration/password_success.html")