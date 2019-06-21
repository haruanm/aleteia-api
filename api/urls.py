from .views import FakeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', FakeViewSet, basename='checker')

urlpatterns = router.urls
