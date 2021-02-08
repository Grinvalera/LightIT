from django.contrib import admin

from .models import Product, Order, Score


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('product_name', 'price', 'end_price', 'date')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('product', 'status_order', 'date_order')


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):

    list_display = ('name', 'date_score')