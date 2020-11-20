from .models import Article, Comments, FavoriteArticle
from django.test import TestCase
from datetime import datetime
User = get_user_model()

class TestModels(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.article = Article.objects.create(user_id=self.user, title='testTitle', body='testBody')
        self.comment = Comments.objects.create(user_id=self.user, article_id=self.article, body='testComment')
    
    def test_article_fields(self):
        self.assertIsInstance(self.article.title, str)
        self.assertIsInstance(self.article.body, str)
        self.assertIsInstance(self.article.create_date, datetime)

    def test_comments_fields(self):
        self.assertIsInstance(self.comment.body, str)
        self.assertIsInstance(self.comment.create_date, datetime)