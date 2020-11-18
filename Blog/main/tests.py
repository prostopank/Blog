from django.http import response
from django.http import request
from django.test import TestCase, Client, RequestFactory, SimpleTestCase
from .models import Article, Comments, FavoriteArticle
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from . import views
from . import forms


User = get_user_model()

#TEST URLS
class TestUrls(SimpleTestCase):

    def test_index_url_is_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.__name__, views.HomeListView.as_view().__name__)

    def test_article_url_is_resolves(self):
        url = reverse('article', args=['1'])
        self.assertEquals(resolve(url).func.__name__, views.ArticleDetail.as_view().__name__)

    def test_editpage_url_is_resolves(self):
        url = reverse('editpage')
        self.assertEquals(resolve(url).func.__name__, views.ArticleEditView.as_view().__name__)
        
    def test_updatepage_url_is_resolves(self):
        url = reverse('updatepage', args=['1'])
        self.assertEquals(resolve(url).func.__name__, views.ArticleUpdateView.as_view().__name__)
    
    def test_deletepage_url_is_resolves(self):
        url = reverse('deletepage', args=['1'])
        self.assertEquals(resolve(url).func.__name__, views.ArticleDeleteView.as_view().__name__)
    
    def test_login_url_is_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.__name__, views.UserLoginView.as_view().__name__)

    def test_register_url_is_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.__name__, views.RegisterUserView.as_view().__name__)
    
    def test_logout_url_is_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.__name__, views.UserLogoutView.as_view().__name__)
    
    def test_logout_url_is_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.__name__, views.UserLogoutView.as_view().__name__)
    
    def test_search_url_is_resolves(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.__name__, views.SearchView.as_view().__name__)
    
    def test_favorite_article_url_is_resolves(self):
        url = reverse('favoritearticle')
        self.assertEquals(resolve(url).func.__name__, views.FavoriteView.as_view().__name__)
    
    def test_add_favorite_article_url_is_resolves(self):
        url = reverse('addfavorite', args=['1'])
        self.assertEquals(resolve(url).func.__name__, views.AddToFavoriteView.as_view().__name__)
    
    
#TEST VIEWS
class TestViews(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.article = Article.objects.create(user_id=self.user, title='testTitle', body='testBody')
        self.comment = Comments.objects.create(user_id=self.user, article_id=self.article, body='testComment')

    def test_home_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_article_detail_view(self):
        response = self.client.get(reverse('article', args=['1']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/article.html')
    

    #TODO 
    """def test_article_update_view(self):
        login = self.client.login(username = self.user.username, password = self.user.password)
        
        response = self.client.post(reverse('updatepage', args='1'), {
            'title': 'updateTitle',
            'body': 'updateBody',
        })
        print(response.context)
        self.assertEqual(str(response.context['user']), self.user.username)
        #article = Article.objects.get(id=2)
        self.assertEquals(response.status_code, 302)
        #self.assertEquals(article.title, 'updateTitle')"""

    #TODO
    #def test_article_delete_view(self):

    
    def test_add_to_favorite_view(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        response = views.AddToFavoriteView.as_view()(request, pk = '1')
        favorite_article = FavoriteArticle.objects.get(id=1)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(favorite_article.article_id, self.article)

    def test_favorite_view(self):
        factory = RequestFactory()
        request = factory.get('favoritearticle')
        request.user = self.user
        response = views.FavoriteView.as_view()(request)
        self.assertEquals(response.status_code, 200)
        
    def test_user_login_view(self):
        login = self.client.login(username = self.user.username, password = self.user.password)
        response = self.client.post(reverse('login'), {
            'username': self.user.username,
            'password': self.user.password
        })
        self.assertTrue(response.context['widget'].get('value'), 'testuser')
    

#TEST FORMS
class TestForms(TestCase):

    def test_article_form_valid_data(self):
        form = forms.ArticleForm(data={
            'title': 'test_title',
            'body': 'test_body',
        })

        self.assertTrue(form.is_valid())

    def test_article_form_no_data(self):
        form = forms.ArticleForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    #TODO
    def test_user_login_form_valid_data(self):
        """self.user = User.objects.create(username='testuser', password='password')
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user"""
        form = forms.LoginUserForm(data={
            'username': 'testuser',
            'password': 'password',
        })
        self.assertTrue(form.is_valid())
    
    def test_user_login_form_no_data(self):
        form = forms.LoginUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
    
    #TODO
    def test_user_register_form_valid_data(self):
        form = forms.LoginUserForm(data={
            'username': 'testuser',
            'password': 'password',
        })
        self.assertTrue(form.is_valid())

    def test_user_register_form_no_data(self):
        form = forms.RegisterUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
    
    def test_comment_form_valid_data(self):
        form = forms.CommentForm(data={
            'body': 'test_body',
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        form = forms.RegisterUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
