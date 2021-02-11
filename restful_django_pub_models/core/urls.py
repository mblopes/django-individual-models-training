from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, CustomerViewSet, \
                   SportViewSet, TeamViewSet


router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'products', ProductViewSet, basename="products")
router.register(r'customers', CustomerViewSet, basename="customers")
router.register(r'sports', SportViewSet, basename="sports")
router.register(r'teams', TeamViewSet, basename="teams")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'
    )),
]
