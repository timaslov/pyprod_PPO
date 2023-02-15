from rest_framework import serializers

from .models import Article, Subject


class ArticleSerializer(serializers.ModelSerializer):
    item = serializers.ReadOnlyField(default="article")

    class Meta:
        model = Article
        exclude = ["content"]


class SubjectAndChildrenSerializer(serializers.ModelSerializer):
    item = serializers.ReadOnlyField(default="subject")
    children = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = "__all__"

    @staticmethod
    def get_children(obj):
        child_articles = obj.articles.defer("content")
        child_subjects = obj.children.all()
        articles_data = ArticleSerializer(child_articles, many=True).data
        subjects_data = SubjectAndChildrenSerializer(child_subjects, many=True).data
        data = list(articles_data) + list(subjects_data)
        return data
