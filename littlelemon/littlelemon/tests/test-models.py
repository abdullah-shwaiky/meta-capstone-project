from django.test import TestCase
from restaurant import models


class MenuTest(TestCase):
    def instance(self):
        item = models.Menu.objects.create(title = 'Icecream', price = 80, inventory = 50)
        self.assertEqual(item, "Icecream : 80")