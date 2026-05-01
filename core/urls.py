from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
