from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class IInterest(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class CCity(models.Model):
    ctitle = models.CharField(max_length=40)

    def __str__(self):
        return self.ctitle


class PPerson(models.Model):
    name = models.CharField(max_length=40)
    mobile = models.CharField(max_length=40)
    interests = models.ManyToManyField(IInterest)
    
    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=40)
    person = models.OneToOneField(PPerson,on_delete=models.CASCADE)
    city = models.ForeignKey(CCity,on_delete=CASCADE) 

    def __str__(self):
        return self.person.name