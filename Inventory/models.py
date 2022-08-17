from django.db import models
from django.urls import reverse
import uuid
from supplier.models import Supplier
# from sales.models import Customer

class Product(models.Model):
	product_code=models.CharField(max_length=40, null=True, blank=True)
	product = models.CharField(max_length=200)
	Quantity = models.IntegerField(max_length=100,default=0,null=True, blank=True)
	discount = models.FloatField(default = 0)
	purchase_price = models.FloatField(null=True, blank=True)
	sale_price = models.FloatField(null=True, blank=True)
	supplier=models.ForeignKey(Supplier,null=True,blank=True, on_delete=models.CASCADE)
	stored_location=models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



	def __str__(self):
		# 
		return f'{self.product}'
		
	@property
	def get_final_price_after_discount(self):
		return (self.sale_price) -  (self.sale_price * (self.discount)/100)

	def get_absolute_url(self):
		return reverse('product-detail', kwargs={'pk': self.pk})


class ProductBulkUpload(models.Model):
	date_uploaded = models.DateTimeField(auto_now=True)
	csv_file = models.FileField(upload_to='inventory/bulkupload/')


class ReturnProduct(models.Model):
	name = models.CharField(max_length=200)
	quantity = models.IntegerField(max_length=100,default=0,null=True, blank=True)

	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	# customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
