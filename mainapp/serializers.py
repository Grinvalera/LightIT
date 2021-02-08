from rest_framework import serializers

from .models import Product, Order, Score


class ProductSerialize(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerialize(serializers.ModelSerializer):

    product = ProductSerialize(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class ScoreSerialize(serializers.ModelSerializer):

    name = OrderSerialize(read_only=True)

    class Meta:
        model = Score
        fields = '__all__'