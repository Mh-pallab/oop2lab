from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    message = models.TextField(max_length=500,null=True)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    phone = models.CharField(max_length=15,null=True)
    device = models.TextField(max_length=100,null=True)
    address = models.TextField(max_length=500,null=True)
    problem = models.TextField(max_length=500,null=True)
    def __str__(self):
        return self.name