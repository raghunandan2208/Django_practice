from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    c_image = models.ImageField(upload_to='products/category', blank = True)

    def __str__(self):
        return self.name


class Item(models.Model):
    status = [
        ("A","Available"),
        ("NA", "Not Available")
        ]
    p_title = models.CharField(max_length = 100, verbose_name = "Product Title")
    p_brand = models.CharField(max_length = 50, verbose_name = "Brand")
    p_description = models.TextField(max_length = 500, verbose_name = "Product Description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    p_status = models.CharField(max_length=2, choices = status, verbose_name = "Status")
    p_offer_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = "Offer Price")
    p_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = "Actual Price")
    p_offers = models.TextField(verbose_name = "Other Offers")
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='products/item', blank = True)

    def __str__(self):
        return self.p_title
