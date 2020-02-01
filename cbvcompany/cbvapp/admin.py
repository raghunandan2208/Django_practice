from django.contrib import admin
from cbvapp.models import Company
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','ceo','location']

admin.site.register(Company,CompanyAdmin)
