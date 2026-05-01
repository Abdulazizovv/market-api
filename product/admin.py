from django.contrib import admin
from product.models import Category, Product

# ==========================================
# Kategoriya Admin Sozlamalari
# ==========================================
class CategoryAdmin(admin.ModelAdmin):
    """
    Kategoriyalarni boshqaruv paneli ko'rinishi.
    """
    # Admin ro'yxatida ko'rinadigan ustunlar
    list_display = ("id", "title", "slug", "created_at", "updated_at")
    
    # Qidiruv maydonlari (title bo'yicha qidirish imkonini beradi)
    search_fields = ("title",)
    
    # Avtomatik to'ldirish: title yozilganda slug ham avtomatik yoziladi
    prepopulated_fields = {"slug": ("title",)}


# ==========================================
# Mahsulot Admin Sozlamalari
# ==========================================
class ProductAdmin(admin.ModelAdmin):
    """
    Mahsulotlarni boshqaruv paneli ko'rinishi.
    """
    # Mahsulotlar ro'yxatida aks etadigan asosiy ustunlar
    list_display = (
        "id",
        "name",
        "category",
        "price",
        "stock",
        "unit",
        "is_active",
        "created_at",
        "updated_at",
    )
    
    # Nomi bo'yicha qidirish imkoniyati
    search_fields = ("name",)
    
    # O'ng tomonda chiqadigan filtrlash paneli
    list_filter = ("category", "is_active")


# ==========================================
# Modellarni Admin Panelga Ro'yxatdan O'tkazish
# ==========================================
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
