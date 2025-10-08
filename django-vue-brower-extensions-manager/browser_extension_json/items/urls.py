 from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
# The endpoint for the Vue app will be /api/items/
router.register(r'items', ItemViewSet) 

urlpatterns = router.urls
