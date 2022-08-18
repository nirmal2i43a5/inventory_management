



from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Inventory.models import Product, ReturnProduct
from datetime import datetime, timedelta
from sales.forms import SaleItemForm
from sales.models import Sales, SalesItem
from supplier.models import Supplier
from sales.models import Customer
from registers.decorators import admin_only


#Show the data on dashboard 
#This page is only accessible to admin
# @login_required
@admin_only
def dashboard(request):
	total_product = Product.objects.count()
	total_returns = ReturnProduct.objects.count()
	total_supplier = Supplier.objects.count()
	total_sales = SalesItem.objects.all()
	# today_customers=Customer.objects.count()
	# total_orders = SalesItem.objects.count()

	today_customers = Customer.objects.filter(
	created_at__gte=datetime.now() - timedelta(days=1)).count()
	today_sales = SalesItem.objects.filter(
		created_at__gte=datetime.now() - timedelta(days=1))

	sales_total_price = 0.00

	for sale in today_sales:
		per_total_price = float(sale.product.sale_price) * sale.quantity
		sales_total_price += per_total_price
	context = {
		'product': total_product,
		'supplier': total_supplier,
		'customer':today_customers,
		'order':today_sales.count(),
		'today_sales_price': sales_total_price,
		'orders':total_sales,
  'total_returns':total_returns

	}
	return render(request, 'index.html', context)


def front_page(request):
	context = {
 
	}
	return render(request, 'front_page.html', context)
