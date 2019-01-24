from django.db import models

class Temperature(models.Model):
    celcius = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    time_stamp = models.DateTimeField(auto_now=True)

class Humidity(models.Model):
    pass