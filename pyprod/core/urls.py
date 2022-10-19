from django.views.generic import RedirectView
from django.urls import path


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="core_subjects")),
]
