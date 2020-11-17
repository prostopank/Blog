from django.conf.urls import url
from django.http import response
from django.test import TestCase, Client, RequestFactory, SimpleTestCase
from .models import Article, Comments
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve, Resolver404
from . import views


User = get_user_model()


"""class BlogTestViewsCases(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create(username='testuser', password='password')
        self.article = Article.objects.create(user_id=self.user, title='testTitle', body='testBody')
        self.comment = Comments.objects.create(user_id=self.user, article_id=self.article, body='testComment')

    def test_home_list_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_article_detail_view(self):
        response = self.client.get(reverse('article', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/article.html')

    def test_add_new_article(self):
        response = self.client.post('/editpage', {
            'user_id': self.user.id,
            'title': 'test_title',
            'body': 'test_body',
        })
        self.assertEquals(response.status_code, 302)

    def test_update_article(self):
        response = self.client.post('/updatepage/1', {
            'user_id': self.user.id,
            'title': 'test_title_2',
            'body': 'test_body_2',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.article.objects.title, 'test_title_2')

    def test_add_new_user(self):
        response = self.client.post('/register', {
            'username': 'test_user',
            'password': 'password',
        })
        self.assertEquals(response.status_code, 302)

    def test_login_user(self):
        login = self.client.login(username='testuser', password='password')
"""

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
    
    

    