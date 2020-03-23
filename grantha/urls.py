from django.urls import path
from .views import (
    home,
    about,
    blog,
    Search,
    busView,
    carView,
 


)

app_name = 'grantha'

urlpatterns = [
    path('', home, name= 'home'),
    path('about/', about, name= 'about'),
    path('blog/<id>/', blog, name= 'blog-detail'),
    path('search/', Search, name='search'),
    path('bus/', busView.as_view(), name='bus'),
    path('car/', carView.as_view(), name='car'),


]