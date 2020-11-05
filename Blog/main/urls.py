from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('article/<int:id>', views.article_detail),
    path('signin', views.sign_in),
    path('editpage', views.edit_page),
    
]
