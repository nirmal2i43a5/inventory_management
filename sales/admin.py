from django.contrib import admin
from .models import *
# Register your models here.


class SalesModel(admin.ModelAdmin):
    list_display = ['customer']

admin.site.register(Sales, SalesModel)
admin.site.register(SalesItem)


class CustomerAdmin(admin.ModelAdmin):
    list_display =['name','sale_code']

admin.site.register(Customer, CustomerAdmin)