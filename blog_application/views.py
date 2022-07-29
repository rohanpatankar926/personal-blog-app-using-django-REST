from unicodedata import category
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Category, Post
from .forms import PostForm,EditForm
# Create your views here.
# def home(request):
#     return render(request,"home.html",{})

class Home(ListView):
    model=Post
    template_name="home.html"
    ordering=["-publication_date"]

    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(Home,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context

class ArticleDetails(DetailView):
    model=Post
    template_name= "article_detail.html"


class AddPostView(CreateView):
    model=Post
    form_class =PostForm
    template_name="add_post.html"
    # fields="__all__

class AddCategoryView(CreateView):
    model=Category
    # form_class =PostForm
    template_name="add_category.html"
    fields="__all__"

class UpdatePost(UpdateView):
    model=Post
    form_class=EditForm
    template_name="update_post.html"


def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    return render(request,"categories_list.html",{"cat_menu_list":cat_menu_list})

def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats.replace("-"," "))
    return render(request,"categories.html",{"cats":cats.title().replace("-"," "),"category_post":category_posts})



class DeletePost(DeleteView):
    model=Post
    template_name="delete_post.html"
    success_url=reverse_lazy("home")