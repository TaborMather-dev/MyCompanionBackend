from django.db import models

# Create your models here.

class Sitter(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    phone_number = models.CharField(max_length=10, blank=False, default='')
    email = models.CharField(max_length=100, blank=False, default='')
    zip_code = models.IntegerField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name