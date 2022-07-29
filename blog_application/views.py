from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,EditForm
# Create your views here.
# def home(request):
#     return render(request,"home.html",{})

class Home(ListView):
    model=Post
    template_name="home.html"
    ordering=["-publication_date"]

class ArticleDetails(DetailView):
    model=Post
    template_name= "article_detail.html"

class AddPostView(CreateView):
    model=Post
    form_class =PostForm
    template_name="add_post.html"
    # fields="__all__"

class AddCategoryView(CreateView):
    model=Post
    # form_class =PostForm
    template_name="add_category.html"
    fields="__all__"

class UpdatePost(UpdateView):
    model=Post
    form_class=EditForm
    template_name="update_post.html"

class DeletePost(DeleteView):
    model=Post
    template_name="delete_post.html"
    success_url=reverse_lazy("home")