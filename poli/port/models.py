from tokenize import group
from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    group = models.CharField(max_length=10)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    
    math = models.CharField(max_length=30)
    physics = models.CharField(max_length=30)
    history = models.CharField(max_length=30)
    biology = models.CharField(max_length=30)
    geography = models.CharField(max_length=30)
    
    math_score = models.IntegerField(default=0)
    physics_score = models.IntegerField(default=0)
    history_score = models.IntegerField(default=0)
    biology_score = models.IntegerField(default=0)
    geography_score = models.IntegerField(default=0)
    all_score = models.IntegerField(default=0)

    def __str__(self):
        return self.name


