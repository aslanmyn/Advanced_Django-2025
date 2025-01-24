from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import User, Project, Category, Priority, Task

from .serializers import UserSerializer, ProjectSerializer, CategorySerializer, PrioritySerializer, TaskSerializer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
import logging

logger = logging.getLogger(__name__)
from .permissions import IsAdmin, IsManager, IsEmployee


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer

    permission_classes = [IsAdmin]


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()

    serializer_class = ProjectSerializer

    permission_classes = [IsManager]


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsEmployee]