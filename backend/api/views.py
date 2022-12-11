from api.serializers import MediaSerializer,SizeSerializer,ColorSerializer,BrandSerializer,CategorySerializer,ProductSerializer,ProductInventorySerializer,StockSerializer
from api.models import Media,Size,Color,Brand,Category,Product,ProductInventory,Stock
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
class ProductInventoryViewSet(viewsets.ModelViewSet):
    serializer_class =ProductInventorySerializer
    queryset = ProductInventory.objects.all()