from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet
from products.viewsets import ProductGenericViewSet

router = DefaultRouter()

# all http methods
# router.register('products', ProductViewSet, basename='products')

# selected http methods
router.register('products', ProductGenericViewSet, basename='products')

print(router.urls)
urlpatterns = router.urls
