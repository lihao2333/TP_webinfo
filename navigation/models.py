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
    image = models.ImageField(upload_to="subsection",null=True ,default=None, blank=True)
    content = models.TextField()
class Block(models.Model):
    image = models.ImageField(upload_to="block")
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Main(models.Model):
    title = models.CharField(max_length=50)
    welcome = models.CharField(max_length=50)
    welcome_sub = models.CharField(max_length=50)
    tele = models.CharField(max_length=50 ,null=True ,default=None, blank=True)
    weibo = models.CharField(max_length=100,null=True ,default=None, blank=True)
    email = models.CharField(max_length=50,null=True ,default=None, blank=True)
    address = models.CharField(max_length=51,null=True ,default=None, blank=True)
    wallpaper = models.ImageField(upload_to="main",null=True ,default=None, blank=True)
    logo = models.ImageField(upload_to="main",null=True ,default=None, blank=True)
    def __str__(self):
        return self.title
