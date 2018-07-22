from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=30)
class Subsection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
