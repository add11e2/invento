from rest_framework import serializers
from api.models import Media,Size,Color,Brand,Category,Product,ProductInventory,Stock

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields= '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields= '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields= '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields= '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= '__all__'

class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields= '__all__'
        depth=1

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields= '__all__'