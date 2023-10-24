from rest_framework.routers import DefaultRouter

from apps.settings.api.views import SettingAPIView


router = DefaultRouter()
router.register('', SettingAPIView, "api_settings")

urlpatterns = router.urls