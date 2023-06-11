from django.db import models

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    descp = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name+" "+self.title

class Blogs(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    slug = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title