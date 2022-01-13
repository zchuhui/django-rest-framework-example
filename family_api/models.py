from django.db import models

# Create your models here.

class Relationship(models.Model):
    '''
        关系模型
    '''
    name = models.CharField(max_length=50)

class Person(models.Model):
    '''
        家人模型
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sex = models.BooleanField()
    age = models.IntegerField()
    birth_date = models.DateField()
    intro = models.TextField(max_length=200)
    relation = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


