from django.db import models
import uuid

class Media(models.Model):
    url = models.CharField(max_length=800)

    def __str__(self):
        return self.url

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    sku = models.UUIDField(
         default = uuid.uuid4,
         editable = False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    media = models.ForeignKey(Media,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    is_on_sale = models.BooleanField()


class Stock(models.Model):
    productinventory = models.ForeignKey(ProductInventory,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    units = models.IntegerField()
    units_sold = models.IntegerField()

    def __str__(self):
        return self.id