from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .. import views


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

    def test_search_url_is_resolves(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.__name__, views.SearchView.as_view().__name__)

    def test_favorite_article_url_is_resolves(self):
        url = reverse('favoritearticle')
        self.assertEquals(resolve(url).func.__name__, views.FavoriteView.as_view().__name__)

    def test_add_favorite_article_url_is_resolves(self):
        url = reverse('addfavorite', args=['1'])
        self.assertEquals(resolve(url).func.__name__, views.AddToFavoriteView.as_view().__name__)
