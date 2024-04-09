from django.db import models

# Create your models here.

#Class airport code and the city to which the aiport belongs 
class Airport(models.Model):
    code = models.CharField(max_length=4)
    city = models.CharField(max_length=64)

#This class holds foreign keys of different Airports
class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination} in {self.duration}"