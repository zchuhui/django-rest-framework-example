from django.db import models


class Hero(models.Model):
    '''
        Hero Model
    '''
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
    
class Company(models.Model):
    '''
        Company model
    '''
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=60)
    fields = models.CharField(max_length=60)
    official_website = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name