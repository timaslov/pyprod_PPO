from django.db.models import QuerySet
from .models import Subject


def get_core_subjects() -> QuerySet:
    return Subject.objects.filter(parent__isnull=True)
