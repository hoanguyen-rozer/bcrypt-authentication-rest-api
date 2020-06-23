from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

STATUS_CHOICES = (
    ('pending', 'PENDING'),
    ('delivery', 'DELIVERY'),
    ('complete', 'COMPLETE')
)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    products = models.ManyToManyField(Product, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)