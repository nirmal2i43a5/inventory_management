



from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Inventory.models import Product
from supplier.models import Supplier
from sales.models import Customer


@login_required
def dashboard(request):
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_order=Customer.objects.count()
    context = {
        'product': total_product,
        'supplier': total_supplier,
        'order':total_order,

    }
    return render(request, 'index.html', context)
