from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer

from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend



class ProductListAPIView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	filter_backends = [
					filters.SearchFilter, 
					filters.OrderingFilter, 
					DjangoFilterBackend
					]
	search_fields = ["title", "description"]
	ordering_fields  = ["title", "price"]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

