from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import User, Article, Subject


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ("title", "tagline", "content")
    list_display = ("title", "slug", "updated_at", "status")
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    fields = [
        "title",
        "tagline",
        "content",
        "slug",
        "subject",
        "status",
        "created_at",
        "updated_at",
    ]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ("title", "description")
    list_display = ("title", "slug", "parent", "updated_at")
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    fields = [
        "title",
        "parent",
        "description",
        "slug",
        "created_at",
        "updated_at",
    ]


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
