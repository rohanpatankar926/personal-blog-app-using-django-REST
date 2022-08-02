from django.urls import path,include

from .models import Category
from .views import AddCategoryView, AddPostView, ArticleDetails, CategoryListView, CategoryView, DeletePost, Home, LikeView, UpdatePost
urlpatterns = [
   path("",Home.as_view(),name="home"),
   path("article/<int:pk>",ArticleDetails.as_view(),name="articles")
   ,path("add_post/",AddPostView.as_view(),name="add_post"),
   path("article/edit/<int:pk>",UpdatePost.as_view(),name="updatepost"),
   path("article/<int:pk>/delete",DeletePost.as_view(),name="deletepost"),
   path("add_category/",AddCategoryView.as_view(),name="add_category"),
   path("category/<str:cats>/",CategoryView,name="category"),
   path("category-list/",CategoryListView,name="categorylist"),
   path("like-post/<int:pk>",LikeView,name="like_post"),
]