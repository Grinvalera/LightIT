from rest_framework import routers

from .api import ProductViewSet, OrderViewSet, ScoreViewSet

router = routers.DefaultRouter()
router.register('api/product', ProductViewSet, 'product')
router.register('api/order', OrderViewSet, 'order')
router.register('api/score', ScoreViewSet, 'score')


urlpatterns = router.urls