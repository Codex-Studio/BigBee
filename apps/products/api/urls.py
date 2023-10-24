from rest_framework.routers import DefaultRouter

from apps.products.api.views import ProductAPIView

router = DefaultRouter()
router.register('product', ProductAPIView, "api_products")

urlpatterns = router.urls