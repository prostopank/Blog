from django.test import TestCase, RequestFactory
from ..models import Article, Comments, FavoriteArticle
from django.urls import reverse
from .. import views
from django.contrib.auth.models import User


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

    def test_article_update_view(self):
        user = User.objects.create_user(username='testuser1', password='12345')
        article = Article.objects.create(user_id=user, title='testTitle1', body='testBody1')

        response = self.client.post(reverse('updatepage', args='2'), {
            'title': 'updateTitle',
            'body': 'updateBody',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(article.title, 'updateTitle')

    def test_add_to_favorite_view(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user

        response = views.AddToFavoriteView.as_view()(request, pk='1')
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
        response = self.client.post(reverse('login'), {
            'username': self.user.username,
            'password': self.user.password
        })

        self.assertTrue(response.context['widget'].get('value'), 'testuser')
