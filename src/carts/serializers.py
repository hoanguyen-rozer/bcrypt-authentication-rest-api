from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Cart

User = get_user_model()


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ('id', 'user', 'products', 'status')
        extra_kwargs = {
            'user': {
                'read_only': True
            }
        }
