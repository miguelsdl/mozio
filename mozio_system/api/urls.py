from django.urls import include, path
from rest_framework import routers
from api.views import ProviderViewSet, ServiceAreaViewSet

router = routers.DefaultRouter()
router.register(r'provider', ProviderViewSet)
router.register(r'polygon', ServiceAreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
