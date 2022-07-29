from django.urls import path,include
from .views import AddCategoryView, AddPostView, ArticleDetails, DeletePost, Home, UpdatePost
urlpatterns = [
   path("",Home.as_view(),name="home"),
   path("article/<int:pk>",ArticleDetails.as_view(),name="articles")
   ,path("add_post/",AddPostView.as_view(),name="add_post"),
   path("article/edit/<int:pk>",UpdatePost.as_view(),name="updatepost"),
   path("article/<int:pk>/delete",DeletePost.as_view(),name="deletepost"),
   path("add_category/",AddCategoryView.as_view(),name="add_category"),
   
]