# URLS for tasks app

from django.urls import path, include
from .views import TaskViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]