from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class bookingView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        items = models.Booking.objects.all()
        serializer = BookingSerializer(items, many = True)
        return Response(serializer.data)
    
class MenuItemView(ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
class SingleMenuItemView(RetrieveAPIView, DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
class BookingViewSet(ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]