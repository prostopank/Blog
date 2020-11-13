from django.http import response
from django.test import TestCase, Client, RequestFactory
from .models import Article, Comments
from django.contrib.auth import get_user_model
from django.urls import reverse
import json

User = get_user_model()

class BlogTestViewsCases(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create(username = 'testuser', password = 'password')
        self.article = Article.objects.create(user_id = self.user, title = 'testTitle', body = 'testBody')
        self.comment = Comments.objects.create(user_id = self.user, article_id = self.article, body = 'testComment')

    
    def test_home_list_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
    
    def test_article_detail_view(self):
        response = self.client.get(reverse('article', args = [self.article.id]))
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

    def test_add_new_user(self):
        response = self.client.post('/register', {
            'username': 'test_user',
            'password': 'password',
        })
        self.assertEquals(response.status_code, 302)
    
 
    def test_login_user(self):
        login = self.client.login(username = 'testuser', password = 'password')
        