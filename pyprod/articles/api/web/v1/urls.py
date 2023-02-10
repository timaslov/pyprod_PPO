from django.urls import path

from . import views

urlpatterns = [
    path("articles/index/", views.ArticlesIndexView.as_view()),
]
