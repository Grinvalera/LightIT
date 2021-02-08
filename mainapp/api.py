from rest_framework import permissions, viewsets

from .models import Product, Order, Score
from .serializers import ProductSerialize, OrderSerialize, ScoreSerialize


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.order_by('date')
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = ProductSerialize


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = OrderSerialize


class ScoreViewSet(viewsets.ModelViewSet):

    queryset = Score.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ScoreSerialize