from django.contrib import admin
from product.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "created_at", "updated_at")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


class ProductAdmin(admin.ModelAdmin):
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
    search_fields = ("name",)
    list_filter = ("category", "is_active")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
