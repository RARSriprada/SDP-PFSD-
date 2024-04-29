from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    genre = models.CharField(max_length=100, default='')
    description = models.TextField(default='')  # Provide a default value
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    availability = models.CharField(max_length=20, default='available')
    image = models.ImageField(upload_to='book_images/', default='')

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)  # Add a default value
    payment_method = models.CharField(max_length=50,default=None)  # Cash on Delivery or UPI, for example
    upi_id = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    # Add more fields as needed, such as transaction details, status, etc.

    def __str__(self):
        return f"Order {self.pk} - {self.book.title} ({self.user.username})"


class Customer(models.Model):
    username = models.CharField(max_length=50, default=None)
    email = models.CharField(max_length=50, default=None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
class custom(models.Model):
    username = models.CharField(max_length=50, default=None)
    email = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.username
