from django.shortcuts import render

# Create your views here.
# productos/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        productos = Product.objects.all()  # obtiene todos los productos
        serializer = ProductSerializer(productos, many=True)  # los convierte a JSON
        return Response(serializer.data)