from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.email


class Product(models.Model):
    CATEGORIES = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.FloatField(null=False, default=0.0)
    category = models.CharField(max_length=50, null=True, blank=True, choices=CATEGORIES)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUSES = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    status = models.CharField(max_length=50, null=True, blank=True, choices=STATUSES)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
