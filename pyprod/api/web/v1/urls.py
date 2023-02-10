from django.urls import path, include


app_name = "v1"

urlpatterns = [
    path("", include("articles.api.web.v1.urls")),
]
