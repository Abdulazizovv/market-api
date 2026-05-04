from rest_framework import serializers
from product.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Category
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.title", read_only=True)
    class Meta:
        model = Product
        fields = ["id", "name", "category_name", "price", "stock"]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = "__all__"