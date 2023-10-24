from rest_framework.routers import DefaultRouter

from apps.shops.api.views import ShopAPIView


router = DefaultRouter()
router.register('', ShopAPIView, "api_shops")

urlpatterns = router.urls