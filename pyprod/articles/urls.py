from django.urls import path

from . import views

urlpatterns = [
    path("", views.CoreSubjectsView.as_view(), name="core_subjects"),
    path("subject/<slug:slug>/", views.SubjectView.as_view(), name="subject"),
    path("<slug:slug>/", views.ArticleView.as_view(), name="article"),
]
