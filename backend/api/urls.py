from api.views import ProductInventoryViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
router = DefaultRouter()
router.register(r'inventory', ProductInventoryViewSet, basename='inventory')
urlpatterns = router.urls

urlpatterns = [path('',include(router.urls))]