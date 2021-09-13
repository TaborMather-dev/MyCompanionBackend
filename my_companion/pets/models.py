from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    species = models.CharField(max_length=50, blank=False, default='')
    breed = models.CharField(max_length=50, blank=False, default='')
    color = models.CharField(max_length=50, blank=False, default='')
    gender = models.CharField(max_length=50, blank=False, default='')

    def __str__(self):
        return self.name