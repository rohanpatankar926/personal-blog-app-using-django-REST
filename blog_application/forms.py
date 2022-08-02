from random import choices
from django import forms
from .models import Post,Category


# choices=[("Machine Learning","Machine Learning"),("Deep Learning","Deep Learning"),("NLP","NLP"),("OpenCV","OpenCV"),("MLOPS","MLOPS"),("Cloud","Cloud")]

choices=Category.objects.all().values_list("name","name")

choice_list=[]
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("title","title_tag","author","article_snippets",'category',"body","header_image")

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control',"value":"","id":"elder","type":"hidden"}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'article_snippets':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class EditForm(forms.ModelForm):
     class Meta:
        model=Post
        fields=("title","title_tag","article_snippets","body")

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'article_snippets':forms.TextInput(attrs={'class':'form-control'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }
