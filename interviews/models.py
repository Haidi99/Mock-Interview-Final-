from django.db import models
from django.utils import timezone as _timezone


class Interview(models.Model):
    """
    Lma al model yshtaghal m7tageen n3ml foreign key m3 al user
    """
    interview_id = models.IntegerField()
    start_date = models.DateTimeField(default=_timezone.now)


class Question(models.Model):
    question = models.TextField(max_length=1000, blank=True)
    compare_text = models.TextField(max_length=1000, blank=True)
    question_period = models.IntegerField()


class Feedback(models.Model):
    feedback_id = models.IntegerField()
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    feedback_text = models.TextField(max_length=1000, blank=True)