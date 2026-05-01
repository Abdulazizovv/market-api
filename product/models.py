from django.db import models
from common.models import BaseModel
from django.utils.text import slugify

# ==========================================
# Mahsulot Kategoriyalari Modeli
# ==========================================
class Category(BaseModel):
    """
    Mahsulotlarni guruhlash uchun ishlatiladigan kategriya modeli.
    Har bir kategoriya o'zining nomi va URL uchun slug'iga ega.
    """
    title = models.CharField(max_length=255, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True, verbose_name="URL kaliti (slug)")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Model saqlanayotganda slug bo'sh bo'lsa, title'dan avtomatik yaratib beradi.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


# ==========================================
# Mahsulot O'lchov Birliklari (Tanlovlar)
# ==========================================
class ProductUnitChoices(models.TextChoices):
    """
    Mahsulot o'lchov birliklari uchun enumeration (tanlov) klassi.
    """
    SHEET = "sheet", "Dona"
    GR = "gramm", "Gramm"
    KG = "kg", "Kilogramm"
    LITR = "litr", "Litr"
    OTHER = "other", "Boshqa"


# ==========================================
# Mahsulotlar (Product) Modeli
# ==========================================
class Product(BaseModel):
    """
    Ombordagi mahsulotlar haqidagi barcha asosiy ma'lumotlarni saqlaydi.
    """
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    description = models.TextField(null=True, blank=True, verbose_name="Tavsif")
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="products",
        verbose_name="Kategoriyasi"
    )
    price = models.PositiveIntegerField(default=0, verbose_name="Narxi")
    stock = models.PositiveIntegerField(default=0, verbose_name="Ombordagi miqdori")
    unit = models.CharField(
        max_length=20, 
        choices=ProductUnitChoices.choices, 
        default=ProductUnitChoices.SHEET,
        verbose_name="O'lchov birligi"
    )
    is_active = models.BooleanField(default=True, verbose_name="Sotuvda bormi?")

    def __str__(self):
        return f"Mahsulot: {self.name}"
    
    def save(self, *args, **kwargs):
        """
        Biznes mantiq: Agar mahsulot zaxirasi (stock) tugasa, 
        avtomatik tarzda uni nofaol (is_active=False) holatga o'tkazadi.
        """
        if self.stock <= 0:
            self.is_active = False
        return super().save(*args, **kwargs)
