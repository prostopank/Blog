from django.db import models


class Article(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    title = models.CharField('title', max_length=100, null=False)
    body = models.TextField('body', null=False)
    

    def __str__(self):
        return self.title

