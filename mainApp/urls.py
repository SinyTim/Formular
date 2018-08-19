from django.urls import path

from . import views


app_name = 'mainApp'

urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    path('news/', views.posts_list, name='posts_list'),
    path('news/page/<int:page_num>/', views.posts_list, name='posts_list'),
    path('news/post/<int:post_id>/', views.post_detail, name='post_detail'),
    # path('catalog/', views.catalog, name='catalog'),
    path('clients/', views.clients, name='clients'),
    path('contacts/', views.contacts, name='contacts'),
]
