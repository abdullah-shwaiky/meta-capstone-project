from django.test import TestCase, Client
from restaurant import models, serializers
from django.contrib.auth.models import User
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        
        self.pizza = models.Menu.objects.create(title='Pizza', price=12.99, inventory=10)
        self.burger = models.Menu.objects.create(title='Burger', price=8.99, inventory=5)
        self.pasta = models.Menu.objects.create(title='Pasta', price=15.99, inventory=7)
        
    def test_getall(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('menu'))
        items = models.Menu.objects.all()
        items = serializers.MenuSerializer(items, many = True)
        self.assertEqual(response.data,items.data)