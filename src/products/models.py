from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=39.99)
    description = models.TextField()

    def __str__(self):
        return self.title
