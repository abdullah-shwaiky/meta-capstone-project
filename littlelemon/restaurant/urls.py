#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name = 'menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name = 'menu item'),
    path('booking/', views.bookingView.as_view(), name = 'booking')
]
