from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Article(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    title = models.CharField('title', max_length=100, null=False)
    body = models.TextField('body', null=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comments(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments_article')
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    body = models.TextField('body', null=False)


class FavoriteArticle(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='favorite_article')
    user_id = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return str(self.id)
