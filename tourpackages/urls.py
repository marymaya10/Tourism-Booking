from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourPackageViewSet

router = DefaultRouter()
router.register(r'', TourPackageViewSet, basename='tourpackage')

urlpatterns = [
    path('', include(router.urls)),
]
