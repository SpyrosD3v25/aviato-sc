'''
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class User(models.Model):

	Required: name, age, sex, height, weight, free_time, current_nutrition, health_problems, current_workout_plan, 
	current_meditation, current_volunteering

	Optional: tireness_history, sleep_schedule, sleep_history, diet_history, nutrition_history, happiness_history, workout_history, 
	meditation_history, volunteering_history
	'''

# from django.db import models

# class ChatMessage(models.Model):
#     message = models.TextField()
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.message

# from django.db import models
# from django.contrib.auth.models import User

from django.db import models

class Person(models.Model):
	username = models.CharField(max_length=130)
	password = models.CharField(max_length=200)
	age = models.IntegerField(null=True)
	weight = models.IntegerField(null=True)
	height = models.IntegerField(null=True)
	health_problems = models.CharField(max_length=200)

class Message(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)