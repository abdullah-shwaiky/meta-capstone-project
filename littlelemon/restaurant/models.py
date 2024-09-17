from django.db import models

# Create your models here.

class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    def __str__(self) -> str:
        return self.name
    
class Menu(models.Model):
    ID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField()
    def __str__(self) -> str:
        return self.title