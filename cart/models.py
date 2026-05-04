from django.db import models
from django.contrib.auth.models import User
from common.models import BaseModel


class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def total_price(self):
        summ = 0
        for item in self.items.all():
            summ += item.total_price
        return summ

    def __str__(self):
        return f"Cart: {self.user.username}"


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    class Meta:
        unique_together = ("cart", "product")