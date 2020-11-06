from django.http import request
from django.shortcuts import redirect, render
from .models import User, Article
from django.views.generic import ListView
from .forms import ArticleForm
from django.urls import reverse

def index(request):
    articles = Article.objects.all()
    template = 'main/index.html'
    context = {
        'articles': articles,
    }
    return render(request, template, context)

def article_detail(request, id):
    get_article = Article.objects.get(id=id)
    template = 'main/article.html'
    context = {
        'get_article': get_article,
    }
    return render(request, template, context)

def edit_page(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()


    articles = Article.objects.all()
    template = 'main/editpage.html'
    context = {
        'list_articles': articles,
        'form': ArticleForm(),
    }
    return render(request, template, context)

def update_page(request, id):

    get_article = Article.objects.get(id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance = get_article)
        if form.is_valid():
            form.save()

    
    template = 'main/editpage.html'
    context = {
        'get_article': get_article,
        'update': True,
        'form': ArticleForm(instance = get_article),
    }
    return render(request, template, context)


def delete_page(request, id):
    get_article = Article.objects.get(id=id)
    get_article.delete()

    return redirect(reverse('editpage'))






def sign_in(request):
    return render(request, 'main/signin.html')

