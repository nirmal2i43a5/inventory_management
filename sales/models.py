from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from random import randrange
import uuid
from Inventory.models import *

CHARSET='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LENGTH=10
MAX_TRIES=32


class Customer(models.Model):
	class Meta:
		verbose_name_plural='Customers'

	name=models.CharField(max_length=200)
	sale_code=models.CharField(max_length=LENGTH, editable=False, unique=True)
	phone_no=models.CharField(max_length=200, null=True)
	email = models.EmailField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('sales-create', kwargs={'pk': self.pk})

	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	#     return reverse('sale-form',kwargs={'pk':self.pk})

	# @property
	# def get_price_total(self):
	#     quantity=self.quantity
	#     price = self.product.sale_price
	#     total_price=quantity*price
	#     return total_price

	def save(self,*args,**kwargs):
		# self.total_price=self.get_price_total
		loop_num=0
		unique=False
		while not unique:
			if loop_num < MAX_TRIES:
				new_code=''
				for i in range(LENGTH):
					new_code+=CHARSET[randrange(0,len(CHARSET))]
				if not Customer.objects.filter(sale_code=new_code):
					self.sale_code=new_code
					unique=True
				loop_num+=1
			else:
				raise ValidationError("Couldn't generate a unique code.")
		super(Customer, self).save(*args,**kwargs)

class Sales(models.Model):
	customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
	date=models.DateField(auto_now_add=True)

	def __str__(self):
		return str(self.customer)

	@property
	def total_order(self):
		order_items = SalesItem.objects.filter(sales_id=self.id)
		sum = 0
		for order_item in order_items:
			sum = sum + order_item.get_price_total
		return sum

	@property
	def total_qty(self):
		order_items = SalesItem.objects.filter(sales_id=self.id)
		total_qty = 0
		for order_item in order_items:
			total_qty = (order_item.quantity + total_qty)
		return total_qty

	@property
	def order_item(self):
		order_item = SalesItem.objects.filter(sales_id=self.id).first()
		return order_item


	def get_absolute_url(self):
		return reverse('sales_details', kwargs={'pk': self.pk})


class SalesItem(models.Model):
	# status=(
	#     ('Pending','Pending'),
	#     ('Delivered','Delivered'),
	#     # ('Out for delivery','out for delivery')   
	# )
	
	class Meta:
		verbose_name_plural='salesitem'
	
	sales_id=models.ForeignKey(Sales, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)
	total_price = models.FloatField(null=True, blank=True)
	# status=models.CharField(max_length=100,null=True,blank=True,choices=status,default='Delivered')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.product}'
	
	# @property
	# def get_specific_price_total(self):
	#     quantity = self.quantity
	#     price = self.product.sale_price
	#     total_price = quantity * price
	#     return total_price
	
	@property
	def get_price_total(self):
		quantity = self.quantity
		price = self.product.sale_price
		total_price = quantity * price
		return total_price
	
	



	@property
	def get_total(self):#particuler orderitem price
		
		return self.quantity * self.product.price
		

	@property
	def get_total_discount_item_price(self):
		return self.quantity * (self.product.sale_price * (self.product.discount)/100)

	#i use decimal field and it is not callable so i use long code 

	@property
	def get_final_price_after_discount(self):
		return (self.quantity * self.product.sale_price) - self.quantity * (self.product.sale_price * (self.product.discount)/100)



	@property
	def total_save_price(self):
		total_save = 0.00
		total_save = self.quantity * (self.product.sale_price * (self.product.discount)/100)
		for price in total_save:
			total_discount_price = total_save + self.quantity * (self.product.sale_price * (self.product.discount)/100)
		return total_save


	def save(self,*args,**kwargs):
		if self.product.discount:
			self.total = self.get_final_price_after_discount
			super(SalesItem, self).save(*args,**kwargs)
		else:
			self.total_price=self.get_price_total
			super(SalesItem, self).save(*args,**kwargs)