# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class NurseRecord(models.Model):
    nurse_day = models.DateTimeField(default=timezone.now)
    urine_time = models.CharField(max_length=5, null=True)
    urine_volume = models.PositiveIntegerField(null=True)
    meal_asa = models.CharField(max_length=100)
    meal_hiru = models.CharField(max_length=100)
    meal_yoru = models.CharField(max_length=100)
    memo = models.TextField
    def __str__(self):
        return self.meal_asa

 