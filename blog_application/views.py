
from unicodedata import category
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Category, Post
from django.http import HttpResponseRedirect
from .forms import PostForm,EditForm
# Create your views here.

def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get("post_id"))
    # post.likes.add(request.user)
    # return HttpResponseRedirect(reverse("articles",args=[str(pk)]))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse("articles",args=[str(pk)]))
    
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
    def get_context_data(self,*args,**kwargs):
        stuff=get_object_or_404(Post,id=self.kwargs["pk"])
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        total_likes=stuff.total_likes()
        cat_menu=Category.objects.all()
        context=super(ArticleDetails,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        context["liked"]=liked
        context["total_likes"]=total_likes

        return context

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