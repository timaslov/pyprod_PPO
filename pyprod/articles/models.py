from django.shortcuts import reverse
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .const import ArticleStatus


class Article(models.Model):
    title = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255, blank=True)
    content = models.TextField(_("content"), blank=True)
    slug = models.SlugField("slug", max_length=64, unique=True, null=True)
    subject = models.ForeignKey("Subject", null=True, blank=True, on_delete=models.SET_NULL, related_name="articles")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    status = models.CharField(choices=ArticleStatus.choices, default=ArticleStatus.DRAFT, max_length=32)
    # tags = models.ManyToManyField("citytags.Tag", through="core.ArticleTag", blank=True)
    # main_photo = models.ForeignKey("Photo", blank=True, null=True, on_delete=models.SET_NULL, related_name="articles")
    # photos = models.ManyToManyField("Photo", through="core.ArticlePhoto", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})


class Subject(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="children")
    description = models.TextField(_("description"), blank=True)
    slug = models.SlugField("slug", max_length=64, unique=True, null=True)
    # photo = models.ForeignKey("Photo", blank=True, null=True, on_delete=models.SET_NULL, related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("subject")
        verbose_name_plural = _("subjects")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("subject", kwargs={"slug": self.slug})
