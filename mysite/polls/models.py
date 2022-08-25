import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


from datetime import date




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








class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline





"""
python manage.py shell
from polls.models import Blog, Entry

# filter
Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)
Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)

# exclude

Blog.objects.exclude(entry__headline__contains='Lennon',entry__pub_date__year=2008)
Blog.objects.exclude(entry__in=Entry.objects.filter(headline__contains='Lennon',pub_date__year=2008,),)
"""













class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]





class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

