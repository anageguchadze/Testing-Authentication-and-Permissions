from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrivateItemViewSet

router = DefaultRouter()
router.register(r'private-items', PrivateItemViewSet, basename='private-item')

urlpatterns = [
    path('', include(router.urls)),
]
