from django.shortcuts import render
from .models import User, Article

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

def sign_in(request):

    return render(request, 'main/signin.html')

