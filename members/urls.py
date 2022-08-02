from django.urls import path,include

from .views import ShowProfilePageView, EditProfilePageView,UserEdit, UserRegister,PasswordsChangeView,CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("register/",UserRegister.as_view(),name="register"),
    path("edit_profile/",UserEdit.as_view(),name="editprofile"),
    path("password/",PasswordsChangeView.as_view(template_name="registration/change_password.html"),name="passwordchange"),
    path("password-success/",views.password_success,name="passwordsuccess"),
    path("<int:pk>/profile/",ShowProfilePageView.as_view(template_name="registration/user_profile.html"),name="showprofilepage"),
    path("<int:pk>/edit-profile-page/",EditProfilePageView.as_view(template_name="registration/edit_profile_page.html"),name="editprofilepageview"),
    path("create_profile/",CreateProfilePageView.as_view(template_name="registration/create_user_profile.html"),name="createprofilepage"),
    
]