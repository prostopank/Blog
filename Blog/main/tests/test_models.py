from ..models import Article, Comments, FavoriteArticle
from django.test import TestCase
from datetime import datetime
from django.contrib.auth.models import User


class TestModels(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.article = Article.objects.create(user_id=self.user, title='testTitle', body='testBody')
        self.comment = Comments.objects.create(user_id=self.user, article_id=self.article, body='testComment')
        self.favorite_article = FavoriteArticle.objects.create(user_id=self.user, article_id=self.article)

    def test_article_model(self):
        self.assertIsInstance(self.article.title, str)
        self.assertIsInstance(self.article.body, str)
        self.assertIsInstance(self.article.create_date, datetime)
        self.assertEquals(str(self.article), self.article.title)

    def test_comments_model(self):
        self.assertIsInstance(self.comment.body, str)
        self.assertIsInstance(self.comment.create_date, datetime)

    def test_favorite_article_model(self):
        self.assertEquals(str(self.favorite_article), str(self.favorite_article.id))
