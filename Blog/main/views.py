from django.http import request
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView
from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView 
from .forms import ArticleForm, LoginUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


class HomeListView(ListView):
    model = Article
    template_name = 'main/index.html'
    context_object_name = 'articles'

class ArticleDetail(DetailView):
    model = Article
    template_name = 'main/article.html'
    context_object_name = 'get_article'

class ArticleEditView(CreateView):
    model = Article
    template_name = 'main/editpage.html'
    form_class = ArticleForm
    success_url = reverse_lazy('editpage')
    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Article.objects.all()
        return super().get_context_data(**kwargs)

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'main/editpage.html'
    form_class = ArticleForm
    success_url = reverse_lazy('editpage')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'main/editpage.html'
    success_url = reverse_lazy('editpage')


class UserLoginView(LoginView):
    template_name = 'main/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('editpage')
    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('editpage')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('editpage')