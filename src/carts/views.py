# from django.shortcuts import render
# from .serializers import CartSerializer

# from rest_framework import filters
# from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class UserListAPIView(generics.ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
# 	filter_backends = [
# 					filters.SearchFilter, 
# 					filters.OrderingFilter, 
# 					DjangoFilterBackend
# 					]
# 	search_fields = ["username"]
# 	ordering_fields  = ["username"]


# class UserRetrieveAPIView(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer


# class UserCreateAPIView(generics.CreateAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

    
        
