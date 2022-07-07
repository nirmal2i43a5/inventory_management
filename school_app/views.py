from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Inventory.models import Product
from supplier.models import Supplier

@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    context = {
        'product': total_product,
        'supplier': total_supplier,

    }
    return render(request, 'index.html', context)