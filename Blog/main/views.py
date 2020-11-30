from django.db.models import F
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from .models import Article, FavoriteArticle
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import ArticleForm, LoginUserForm, RegisterUserForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class HomeListView(ListView):
    model = Article
    template_name = 'main/index.html'
    context_object_name = 'articles'


class ArticleDetail(FormMixin, DetailView):
    model = Article
    template_name = 'main/article.html'
    context_object_name = 'get_article'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        # Article.objects.filter(id=self.get_object().id).update(views=F("views") + 1)
        # print(request.method)
        return reverse_lazy('article', kwargs={'pk': self.get_object().id})

    def get(self, request, *args, **kwargs):
        statute = super().get_object()
        statute.views += 1
        statute.save()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article_id = self.get_object()
        self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleEditView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Article
    template_name = 'main/editpage.html'
    form_class = ArticleForm
    success_url = reverse_lazy('editpage')

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Article.objects.all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'main/editpage.html'
    form_class = ArticleForm
    success_url = reverse_lazy('editpage')

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].user_id:
            return self.handle_no_permission()
        return kwargs


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'main/editpage.html'
    success_url = reverse_lazy('editpage')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.user_id:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class AddToFavoriteView(View):

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        article_id = kwargs.get('pk')
        if FavoriteArticle.objects.filter(article_id=article_id, user_id=user_id):
            return HttpResponseRedirect(reverse_lazy('favoritearticle'))
        else:
            FavoriteArticle.objects.create(
                user_id_id=user_id, article_id_id=article_id
            )
        return HttpResponseRedirect(reverse_lazy('favoritearticle'))


class FavoriteView(View):

    def get(self, request, *args, **kwargs):
        favorite_articles = FavoriteArticle.objects.all()
        context = {
            'fav': favorite_articles,
        }
        return render(request, 'main/favoritearticle.html', context)


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


class SearchView(ListView):
    template_name = 'main/search.html'

    def get_queryset(self):
        return Article.objects.filter(title__icontains=self.request.GET.get("search"))
