import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin




class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="Question Text")
    pub_date = models.DateTimeField('date published')
    

    
    def __str__(self):
        return self.question_text

    @admin.display(boolean=True,ordering='pub_date',
        description='Published Recently?',)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text






class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


