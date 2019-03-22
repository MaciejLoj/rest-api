from rest_framework.test import APIRequestFactory, force_authenticate
from ..views import ExamsView
from ..models import Exam
from django.test import TestCase
from django.contrib.auth.models import User


class ExamViewTest(TestCase):

    def test_get_exam(self):
        request = APIRequestFactory().get("")
        exam_detail = ExamsView.as_view({'get': 'retrieve'})
        exam = Exam.objects.create(owner=User.objects.create_user('ala', '', password='restapi'),
                                   first_task_points=4, second_task_points=2,sum_of_points=6, grade=3)
        response = exam_detail(request, pk=exam.pk)
        self.assertEqual(response.status_code, 200)

    def test_post_exam(self):
        factory = APIRequestFactory()
        request = factory.post('/exams/', {'sum_of_points': 2}, format='json')
        user = User.objects.create_user('ala', '', password='restapi')
        force_authenticate(request, user=user)
        view = ExamsView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 201)
