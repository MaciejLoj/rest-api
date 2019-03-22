from django.test import TestCase
from ..models import Exam
from django.contrib.auth.models import User


class ExamTest(TestCase):

    def setUp(self):
        Exam.objects.create(
            owner=User.objects.create_user('maciek', '', password='restapi'), first_task_points=4,
            second_task_points=2,sum_of_points=6, grade=3)
        Exam.objects.create(
            owner=User.objects.create_user('ala', '', password='restapi'), first_task_points=3,
            second_task_points=1, sum_of_points=4, grade=2)

    def test_exams(self):
        points_maciek = Exam.objects.get(sum_of_points=6)
        points_ala = Exam.objects.get(sum_of_points=4)

        self.assertEqual(
            points_maciek.get_exams(), 6)
        self.assertEqual(
            points_ala.get_exams(), 4)
