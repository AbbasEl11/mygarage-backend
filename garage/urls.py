from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet

router = DefaultRouter()
router.register('cars', CarViewSet, basename='car')      # statt 'garage/cars'

urlpatterns = [
    path('', include(router.urls)),
    # Wenn Du das custom action upload-images bequem via ViewSet route:
    path(
        'cars/<int:pk>/upload-images/',
        CarViewSet.as_view({'post': 'upload_images'}),
        name='car-upload-images'
    ),
]
