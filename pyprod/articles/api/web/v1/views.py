from dataclasses import asdict

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from ....dal import get_core_subjects
from ....models import Article
from ....serializers import ArticleTreeSerializer, ArticleSerializer, ArticleCreateSerializer
from ....bl import ArticleService
from ....da import ArticleRepository


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all().order_by("-created_at")
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False)
    def index(self, request):
        core_subjects = get_core_subjects()
        result = []
        for core_subject in core_subjects:
            result.append(ArticleTreeSerializer(core_subject).data)

        return Response(result)


class ArticleTestView(APIView):
    serializer_class = ArticleCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        article_service = ArticleService(ArticleRepository())
        article_service.add(article)
        return Response(asdict(article))

