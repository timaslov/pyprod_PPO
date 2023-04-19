from rest_framework import serializers

from .models import Article
from .const import ARTICLE_TREE_FIELDS, ArticleStatus
from .dto import ArticleDTO


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "title",
            "tagline",
            "content",
            "slug",
            "author",
            "status",
            "created_at",
            "updated_at",
        ]


class ArticleCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    tagline = serializers.CharField()
    content = serializers.CharField()
    slug = serializers.CharField()
    parent_id = serializers.IntegerField(required=False)
    author_id = serializers.IntegerField()
    status = serializers.ChoiceField(ArticleStatus.choices)

    def create(self, validated_data):
        return ArticleDTO(**validated_data)


class ArticleTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = list(ARTICLE_TREE_FIELDS) + ["children"]

    @staticmethod
    def get_children(obj):
        child_articles = obj.children.only(*ARTICLE_TREE_FIELDS)
        return ArticleTreeSerializer(child_articles, many=True).data
