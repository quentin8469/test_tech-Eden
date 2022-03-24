from rest_framework.routers import DefaultRouter
from product.views import ProductViewset


router = DefaultRouter()
router.register(r"", ProductViewset, basename='catalogue')

urlpatterns = router.urls
