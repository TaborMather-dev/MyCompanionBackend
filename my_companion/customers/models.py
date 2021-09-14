from django.db import models

# Create your models here.
class Customer(models.Model):
    
    name = models.CharField(max_length=100, blank=False, default='')
    phone_number = models.CharField(max_length=10, blank=False, default='')
    email = models.CharField(max_length=100, blank=False, default='')
    street_address = models.CharField(max_length=50, blank=False, default='')
    city = models.CharField(max_length=50, blank=False, default='')
    state = models.CharField(max_length=50, blank=False, default='')
    zip_code = models.IntegerField()

    def __str__(self):
        return self.name