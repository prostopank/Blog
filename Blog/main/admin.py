from django.contrib import admin
from .models import Article, Comments, SavedArticles, User


admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comments)
admin.site.register(SavedArticles)

