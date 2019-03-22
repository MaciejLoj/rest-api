from rest_framework import serializers
from .models import Exam
from django.contrib.auth.models import User


class ExamsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Exam
        fields = ("owner", "first_task_points", "second_task_points",
                  "sum_of_points", "grade")


class UserSerializer(serializers.ModelSerializer):
    exams = serializers.PrimaryKeyRelatedField(many=True, queryset=Exam.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'exams')

