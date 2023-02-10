from rest_framework import serializers

from .models import Article, Subject


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ["content"]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
