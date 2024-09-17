from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    def __str__(self) -> str:
        return f'Booking: {self.name} with {self.no_of_guests - 1} others'
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'