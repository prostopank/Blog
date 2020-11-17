from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('article/<int:pk>', views.ArticleDetail.as_view(), name='article'),
    path('editpage', views.ArticleEditView.as_view(), name='editpage'),
    path('updatepage/<int:pk>', views.ArticleUpdateView.as_view(), name='updatepage'),
    path('deletepage/<int:pk>', views.ArticleDeleteView.as_view(), name='deletepage'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('register', views.RegisterUserView.as_view(), name='register'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    path('search', views.SearchView.as_view(), name='search'),
    path('favoritearticle', views.FavoriteView.as_view(), name='favoritearticle'),
    path('addfavorite/<int:pk>', views.AddToFavoriteView.as_view(), name='addfavorite'),
    
]
