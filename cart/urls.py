from rest_framework.routers import DefaultRouter
from cart.views import CartViewset


router = DefaultRouter()
router.register(r"", CartViewset, basename='cart')

urlpatterns = router.urls