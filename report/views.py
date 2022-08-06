from django.shortcuts import render
from sales.models import Customer,Product
from django.db.models import Sum
# Create your views here.


#
def view_customer_report(request):
    customers=Customer.objects.all()
    return render(request,'reports/customers_report.html',{'customers':customers})


def each_customer_sales_report(request,id):
    customer = Customer.objects.get(pk = id)
    sales=customer.sales_set.all().order_by('-id')
    context = {
        'sales':sales,
        'customer':customer
    }
    return render(request,'reports/each_customer_sales_report.html',context)


#This is the logic for the product report
def product_report(request):
  products = Product.objects.all()
  sales_quantity_dataset = []
  for product in products:
    product = Product.objects.get(pk = product.id)
    sales_quantity = product.salesitem_set.all().aggregate(Sum('quantity'))
    print(sales_quantity['quantity__sum'])
    # total_product = sales_quantity['quantity__sum'] + int(product.Quantity)
    sales_quantity_dataset.append({
        # 'total_product':total_product,
    'product':product,
    'sales_quantity':sales_quantity['quantity__sum']})

    context = {
        'sales_quantity_dataset':sales_quantity_dataset,
    }

  return render(request, 'reports/product_report.html',context)