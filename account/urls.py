from rest_framework import routers
from .views import AccountViewSet

router = routers.DefaultRouter()
router.register(r'', AccountViewSet)
urlpatterns = router.urls
