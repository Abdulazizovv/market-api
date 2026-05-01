from rest_framework import viewsets
from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer # ProductSerializer bor deb hisoblaymiz

# ==========================================
# Kategoriya ViewSet (API boshqaruvi)
# ==========================================
class CategoryViewSet(viewsets.ModelViewSet):
    """
    Kategoriyalar bilan bog'liq barcha API amallarini bajaruvchi klass.
    
    Ushbu bitta klass orqali quyidagi amallar avtomatik yaratiladi:
    - GET /categories/ (Ro'yxatni ko'rish)
    - POST /categories/ (Yangi kategoriya yaratish)
    - GET /categories/{id}/ (Bitta kategoriyani ko'rish)
    - PUT/PATCH /categories/{id}/ (O'zgartirish)
    - DELETE /categories/{id}/ (O'chirish)
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ==========================================
# Mahsulotlar ViewSet (API boshqaruvi)
# ==========================================
class ProductViewSet(viewsets.ModelViewSet):
    """
    Mahsulotlar bilan bog'liq barcha CRUD amallarini bajaruvchi klass.
    Faqat faol mahsulotlarni ko'rsatish mantiig'i bilan.
    """
    # Bazadan ma'lumotlarni qanday tartibda olish
    queryset = Product.objects.all().order_by('-created_at')
    
    # Ma'lumotlarni JSON formatiga o'giruvchi klass
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Ixtiyoriy: API orqali faqat faol (is_active=True) mahsulotlarni 
        yuborish uchun filtr qo'shish mumkin.
        """
        return Product.objects.filter(is_active=True)
