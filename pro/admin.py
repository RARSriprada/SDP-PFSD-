from django.contrib import admin
from .models import Order, Customer, Book, custom

# Register your models here.


admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(custom)