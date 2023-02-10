from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import Article, Subject
from ....serializers import ArticleSerializer, SubjectSerializer


class ArticlesIndexView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.defer("content")
        subjects = Subject.objects.all()

        articles_data = ArticleSerializer(articles, many=True).data
        subjects_data = SubjectSerializer(subjects, many=True).data

        return Response(articles_data)
