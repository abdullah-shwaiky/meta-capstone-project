#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name = 'menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name = 'menu item'),
    path('booking/', views.bookingView.as_view(), name = 'booking'),
    path('api-token-auth/', obtain_auth_token)
]
