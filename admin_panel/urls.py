from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.article_admin, name='admni_articles')
]