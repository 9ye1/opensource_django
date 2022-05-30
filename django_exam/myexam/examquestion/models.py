from django.db import models

# 문제 정보
class Question(models.Model):
    question = models.CharField(max_length=300)
    choice1 = models.CharField(max_length=50)
    choice2 = models.CharField(max_length=50)
    choice3 = models.CharField(max_length=50)
    choice4 = models.CharField(max_length=50)
    choice5 = models.CharField(max_length=50)
    answer = models.IntegerField(default=1)
    def __str__(self):
        return self.question

class Person(models.Model):
    name = models.CharField(max_length=20)
    ans1 = models.IntegerField(default=0)
    ans2 = models.IntegerField(default=0)
    ans3 = models.IntegerField(default=0)
    ans4 = models.IntegerField(default=0)
    ans5 = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name

