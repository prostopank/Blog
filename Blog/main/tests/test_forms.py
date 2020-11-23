from django.test import TestCase, RequestFactory
from main import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


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
        self.user = User.objects.create(username='testuser', password='password')
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
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