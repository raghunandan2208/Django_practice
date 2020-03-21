from django.contrib import admin
from products.models import Category, Item
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_title', 'p_offer_price', 'category', 'p_status')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
