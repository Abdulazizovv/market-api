from rest_framework import serializers
from product.models import Category, Product

# ==========================================
# Kategoriya Serializer (Ma'lumotlarni o'girish)
# ==========================================
class CategorySerializer(serializers.ModelSerializer):
    """
    Category modelini JSON formatiga o'tkazish va validatsiya qilish.
    """
    
    # slug faqat o'qish uchun (read_only), chunki u save() metodida 
    # avtomatik yaratiladi, foydalanuvchidan kiritish talab qilinmaydi.
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        # Modelning barcha maydonlarini API'ga chiqarish (id, title, slug, created_at, etc.)
        fields = "__all__"


# ==========================================
# Mahsulot Serializer (Ma'lumotlarni o'girish)
# ==========================================
class ProductSerializer(serializers.ModelSerializer):
    """
    Product modelini JSON formatiga o'tkazish va validatsiya qilish.
    """
    
    # Kategoriyaning nomini ko'rish uchun (ixtiyoriy, agar id emas nom kerak bo'lsa)
    category_name = serializers.ReadOnlyField(source='category.title')

    class Meta:
        model = Product
        # Kerakli maydonlarni ro'yxat ko'rinishida ko'rsatish
        fields = (
            "id", 
            "name", 
            "description", 
            "category", 
            "category_name", 
            "price", 
            "stock", 
            "unit", 
            "is_active", 
            "created_at"
        )
        
    def validate_price(self, value):
        """
        Narxni tekshirish (Custom Validation):
        Narx manfiy bo'lishi mumkin emas.
        """
        if value < 0:
            raise serializers.ValidationError("Narx manfiy bo'lishi mumkin emas!")
        return value
