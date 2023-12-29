from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization_name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    service_needed = models.TextField(blank=True)


class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    number =  models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes')
