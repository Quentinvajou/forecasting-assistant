import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    """
    Question within for the poll
    """
    question_text = models.CharField(max_length=200)
    publication_date= models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    

    @admin.display(
            boolean=True,
            ordering="publication_date",
            description= "published recently ?"
    )    
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.publication_date >= now - datetime.timedelta(days=1)

class Choice(models.Model):
    """
    Choice is an answer to a question
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
