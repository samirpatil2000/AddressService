from django.db import models

# Create your models here.

class Address(models.Model):

    name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=300)
    address_line_2 = models.CharField(max_length=300, blank=True, null=True)
    zipcode = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class LatLong(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    request_id = models.IntegerField()
    created_at = models.DateTimeField(verbose_name='date of creation', auto_now_add=True)

    def __str__(self):
        return self.latitude + " - " + self.longitude