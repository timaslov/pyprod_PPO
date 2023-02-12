from rest_framework import serializers

from .models import Article, Subject


class ArticleSerializer(serializers.ModelSerializer):
    item = serializers.ReadOnlyField(default="article")

    class Meta:
        model = Article
        exclude = ["content"]


class SubjectSerializer(serializers.ModelSerializer):
    item = serializers.ReadOnlyField(default="subject")

    class Meta:
        model = Subject
        fields = "__all__"
