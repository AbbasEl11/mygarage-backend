# garage/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from .models import Car, CarImage
from .serializers import CarSerializer, CarImageSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset         = Car.objects.all()
    serializer_class = CarSerializer
    parser_classes   = [JSONParser]

    @action(
        detail=True,
        methods=['post'],
        url_path='upload-images',
        parser_classes=[MultiPartParser, FormParser]
    )
    def upload_images(self, request, pk=None):
        car = self.get_object()
        files = request.FILES.getlist('images')
        for f in files:
            CarImage.objects.create(car=car, image=f)
        return Response(status=status.HTTP_204_NO_CONTENT)
