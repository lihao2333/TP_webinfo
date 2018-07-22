from django.db import models
class Section(models.Model):
    name = models.CharField(max_length=30)
class Subsection(models.Model):
    section = models.ForignKey(Section, on_delete=models.CASCADE)
    name = models.CharFiled(max_length=30)
    url = models.CharFiled(max_length=50)
