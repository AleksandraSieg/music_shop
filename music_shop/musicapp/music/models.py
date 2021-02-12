from django.db import models

# Create your models here.

class Cd(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=40, default='anonimous')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='no description')

    def __str__(self):
        return self.name
