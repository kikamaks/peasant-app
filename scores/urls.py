from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'peasants', views.PeasantViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("scores/", views.PeasantViewSet, name="scores")
]
