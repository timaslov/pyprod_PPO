from rest_framework import routers

from django.urls import path, include

from . import views

router = routers.SimpleRouter()
router.register(r"articles", views.ArticleViewSet, basename="article")


urlpatterns = [
    path("", include(router.urls)),
    path("articles/index/", views.ArticlesIndexView.as_view()),
]
