from rest_framework import routers

from django.urls import path, include

from . import views

router = routers.SimpleRouter()
router.register("", views.ArticleViewSet, basename="article")


urlpatterns = [
    path("test/", views.ArticleTestView.as_view()),
    path("", include(router.urls)),
]
