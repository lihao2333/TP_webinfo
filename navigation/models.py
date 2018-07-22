from django.db import models

# Create your models here.
class Section(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)
class Subsection(models.Model):
    def __str__(self):
        return self.name
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
