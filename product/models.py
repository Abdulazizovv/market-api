from django.db import models
from common.models import BaseModel
from django.utils.text import slugify


class Category(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save()


class ProductUnitChoices(models.TextChoices):
    SHEET = "sheet", "Dona"
    GR = "gramm", "Gramm"
    KG = "kg", "Kilogramm"
    LITR = "litr", "Litr"
    OTHER = "other", "Boshqa"


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=20, choices=ProductUnitChoices.choices, default=ProductUnitChoices.SHEET)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Product: " + self.name
    
    def save(self):
        if self.stock <= 0:
            self.is_active = False
        return super().save()