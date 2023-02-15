from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response

from ....dal import get_core_subjects
from ....models import Article
from ....serializers import SubjectAndChildrenSerializer, ArticleSerializer


class ArticlesIndexView(APIView):
    def get(self, request, *args, **kwargs):
        core_subjects = get_core_subjects()
        result = []
        for core_subject in core_subjects:
            result.append(SubjectAndChildrenSerializer(core_subject).data)

        return Response(result)


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all().order_by("-created_at")
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
