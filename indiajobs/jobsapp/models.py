from django.db import models

# Create your models here.
class IndiaJobs(models.Model):
    title = models.CharField(max_length = 50)
    company = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    experience = models.IntegerField()
    salary = models.IntegerField()
