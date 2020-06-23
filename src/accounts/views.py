from django.shortcuts import render
from .serializers import UserSerializer, AuthBcryptTokenSerializer
from .models import Bcrypt
from .authentication import BcryptTokenAuthentication

from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import action

User = get_user_model()


class UserListAPIView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticated, )
	authentication_classes = (BcryptTokenAuthentication, )

	filter_backends = [
					filters.SearchFilter, 
					filters.OrderingFilter, 
					DjangoFilterBackend
					]
	search_fields = ["username"]
	ordering_fields  = ["username"]


class UserRetrieveAPIView(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	authentication_classes = (BcryptTokenAuthentication, )
	permission_classes = (IsAuthenticated, )

	def get_queryset(self):
		user = self.request.user
		return User.objects.filter(pk=user.pk)


class UserCreateAPIView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class ObtainAuthBcryptToken(ObtainAuthToken):
	serializer_class = AuthBcryptTokenSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data, 
										context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Bcrypt.objects.get_or_create(user=user)
		return Response({'token': token.key})


class LoginAPIView(APIView):

	serializer_class = AuthBcryptTokenSerializer

	def post(self, request):
		return ObtainAuthBcryptToken().post(request)    
        

@action(detail=False, methods=['POST'])
def logoutUser(self, request):
	try:
		request.user.bcrypt_token.delete()
	except AttributeError:
		raise AttributeError("No")
	logout(request)

	return Response({"success": _("Successfully logged out.")},
                    status=status.HTTP_200_OK)
