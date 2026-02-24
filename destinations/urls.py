from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet, BookingViewSet, ReviewListCreateView

router = DefaultRouter()
router.register(r'destinations', DestinationViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
]
