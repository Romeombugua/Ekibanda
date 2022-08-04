from django.contrib import admin
from .models import Category, Order, Customer, Products

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Category)


# Register your models here.
