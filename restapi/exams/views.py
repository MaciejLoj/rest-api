from rest_framework import viewsets
from .models import Exam
from .serializers import ExamsSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class ExamsView(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    filter_fields = ('first_task_points', 'second_task_points', 'sum_of_points',
                     'grade', 'owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


