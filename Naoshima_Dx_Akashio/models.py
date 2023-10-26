from django.db import models

class DoData(models.Model):
    sensorID = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    value = models.FloatField()
    raspberryPIid = models.CharField(max_length=255)

class WaterproofData(models.Model):
    sensorID = models.CharField(max_length=255)
    value = models.FloatField()
    timestamp = models.DateTimeField()
    raspberryID = models.CharField(max_length=255)
