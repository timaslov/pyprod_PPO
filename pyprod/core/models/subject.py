from django.db import models
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="children")
    description = models.TextField(_("description"), blank=True)
    slug = models.SlugField("slug", max_length=64, unique=True, null=True)
    # main_photo = models.ForeignKey("Photo", blank=True, null=True, on_delete=models.SET_NULL, related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("subject")
        verbose_name_plural = _("subjects")

    def __str__(self):
        return self.title
