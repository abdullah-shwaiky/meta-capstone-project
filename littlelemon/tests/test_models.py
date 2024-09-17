from django.test import TestCase
from restaurant import models
from datetime import datetime

class MenuTest(TestCase):
    def test_instance(self):
        item = models.Menu.objects.create(title = 'Icecream', price = 80, inventory = 50)
        self.assertEqual(str(item), "Icecream : 80")

class BookingTest(TestCase):
    def test_booking(self):
        booking = models.Booking.objects.create(name = 'Abdullah', no_of_guests = 3, booking_date = datetime.now())
        self.assertEqual('Booking: Abdullah with 2 others', str(booking))