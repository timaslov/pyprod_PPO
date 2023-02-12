from rest_framework.views import APIView
from rest_framework.response import Response

from ....dal import get_core_subjects
from ....serializers import SubjectAndChildrenSerializer


class ArticlesIndexView(APIView):
    def get(self, request, *args, **kwargs):
        core_subjects = get_core_subjects()
        result = []
        for core_subject in core_subjects:
            result.append(SubjectAndChildrenSerializer(core_subject).data)

        return Response(result)
