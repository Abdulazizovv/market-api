from django.db import models

# ==========================================
# Kuchaytirilgan Asosiy Model (BaseModel)
# ==========================================
class BaseModel(models.Model):
    """
    Barcha modellar uchun umumiy bo'lgan maydonlar va metodlar to'plami.
    Ushbu model bazada alohida jadval yaratmaydi (abstract=True).
    """
    
    # Avtomatik ravishda yaratilgan va tahrirlangan vaqtni saqlaydi
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Yaratilgan vaqt",
        help_text="Obyekt yaratilgan vaqt avtomatik belgilanadi"
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Tahrirlangan vaqt",
        help_text="Obyekt har safar tahrirlanganda ushbu vaqt yangilanadi"
    )

    class Meta:
        # Bu juda muhim: Ushbu model uchun alohida jadval yaratilmaydi.
        # Undan meros olgan modellar ichiga ushbu maydonlar qo'shiladi.
        abstract = True

    # ------------------------------------------
    # Qo'shimcha foydali metodlar (Kuchaytirish)
    # ------------------------------------------

    def get_model_name(self):
        """Model nomini qaytaradi (masalan, 'Product' yoki 'Category')"""
        return self.__class__.__name__

    def update_fields(self, **kwargs):
        """
        Obyekt maydonlarini tezkor yangilash uchun qulay metod.
        Ishlatilishi: instance.update_fields(price=5000, stock=10)
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        return self.save()

    @property
    def is_updated(self):
        """Obyekt yaratilgandan keyin tahrirlanganmi yoki yo'qligini tekshiradi"""
        return self.updated_at > self.created_at
