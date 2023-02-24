from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
    # 3rd-party
    path("tinymce/", include("tinymce.urls")),
]
