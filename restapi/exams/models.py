from django.db import models


class Exam(models.Model):
    GRADE_OPTIONS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    # student = models.CharField(max_length=50,unique=True)
    first_task_points = models.PositiveIntegerField()
    second_task_points = models.PositiveIntegerField()
    sum_of_points = models.PositiveIntegerField()
    grade = models.CharField(max_length=64, null=False, blank=False, choices=GRADE_OPTIONS)
    owner = models.ForeignKey('auth.User', related_name='exams', on_delete=models.CASCADE)

    def get_exams(self):
        return str(self.sum_of_points)

    def __str__(self):
        return str(self.owner)
