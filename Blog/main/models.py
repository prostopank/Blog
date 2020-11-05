from django.db import models

class User(models.Model):
    name = models.CharField('name', max_length=50, null=False)
    email = models.CharField('email', max_length=100, null=False)
    password = models.CharField('password', max_length=50, null=False)

    def __str__(self):
        return self.name

class Article(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    title = models.CharField('title', max_length=100, null=False)
    body = models.TextField('body', null=False)
    

    def __str__(self):
        return self.title

class Comments(models.Model):
    body = models.TextField('body', null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class SavedArticles(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)