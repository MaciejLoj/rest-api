import factory
from django.contrib.auth.models import User

from .models import Exam


class ExamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Exam

    student = factory.Sequence(lambda n: f'student{0}')