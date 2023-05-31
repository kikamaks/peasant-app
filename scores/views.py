import json
from django.http import HttpResponse
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Peasant
from .serializers import PeasantSerializer


def index(request):
    return HttpResponse("Scores app live")


class PeasantViewSet(viewsets.ModelViewSet, mixins.ListModelMixin):
    queryset = Peasant.objects.all()
    serializer_class = PeasantSerializer

    @action(url_name="set_scores", url_path="set_scores", detail=True, methods=["PATCH"])
    def set_scores(self, request, pk):
        user = Peasant.objects.get(id=pk)
        user.score += request.data["score"]
        user.achievements += f"{request.data['achievement']}\n"
        user.save(update_fields=["score", "achievements"])
        return Response(status=status.HTTP_200_OK)

    @action(url_name="login", url_path="login", detail=False, methods=["POST"])
    def login(self, request, pk=None):
        user = Peasant.objects.get(username=request.data["username"])
        password = user.password
        if password != request.data["password"]:
            ...
        return Response(status=status.HTTP_200_OK)
