from django.contrib import admin
from api.models import Media,Size,Color,Brand,Category,Product,ProductInventory,Stock
# Register your models here.
admin.site.register(Media)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(Stock)