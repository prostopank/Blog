from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('article/<int:id>', views.article_detail, name='article'),
    path('signin', views.sign_in, name='signin'),
    path('editpage', views.edit_page, name='editpage'),
    path('updatepage/<int:id>', views.update_page, name='updatepage'),
    path('deletepage/<int:id>', views.delete_page, name='deletepage'),
    
]
