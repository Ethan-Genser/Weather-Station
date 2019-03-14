from django.db import models

class Temperature(models.Model):
    celcius = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.celcius)

class Humidity(models.Model):
    percent = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.percent)

class Pressure(models.Model):
    bar = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.bar)