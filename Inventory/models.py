from django.db import models
from django.urls import reverse
import uuid
from supplier.models import Supplier

class Product(models.Model):
    product_code=models.CharField(max_length=40, null=True, blank=True)
    product = models.CharField(max_length=200)
    Quantity = models.FloatField(max_length=100,default=0,null=True, blank=True)
    purchase_price = models.FloatField(null=True, blank=True)
    sale_price = models.FloatField(null=True, blank=True)
    supplier=models.ForeignKey(Supplier,null=True,blank=True, on_delete=models.CASCADE)
    stored_location=models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)



    def __str__(self):
        return f' {self.product} '

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


class ProductBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to='inventory/bulkupload/')
