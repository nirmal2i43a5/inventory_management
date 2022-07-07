from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy


from .models import Product
import io,csv

@login_required
def inventory_list(request):
  products = Product.objects.all()
  return render(request, 'inventory/product_list.html',{'products':products})


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "inventory/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context


class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    template_name = "inventory/product_form.html"
    fields = '__all__'
    success_message = "New product successfully added."

    def get_form(self):
        '''add date picker in forms'''
        form = super(ProductCreateView, self).get_form()
        form.fields['product'].widget = widgets.Textarea(attrs={'rows': 1})
        # form.fields['unit'].widget = widgets.NumberInput(attrs={'rows': 1})
        form.fields['purchase_price'].widget = widgets.NumberInput(attrs={'rows': 1})
        form.fields['sale_price'].widget = widgets.NumberInput(attrs={'rows': 1})
        # form.fields['supplier'].widget = widgets.MultiWidget(attrs={'rows': 1})
        form.fields['description'].widget = widgets.Textarea(attrs={'rows': 2})
        return form


class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    template_name = "inventory/product_form.html"

    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        form = super(ProductUpdateView, self).get_form()
        form.fields['product'].widget = widgets.Textarea(attrs={'rows': 2})
        form.fields['description'].widget = widgets.Textarea(attrs={'rows': 2})

        return form


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "inventory/product_confirm_delete.html"

    success_url = reverse_lazy('inventory_list')

class ProductBulkUploadView(View):
    def get(self, request):
        template_name = 'inventory/products_upload.html'
        return render(request,template_name)

    def post(self, request):
        paramFile = io.TextIOWrapper(request.FILES['productfile'].file)
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        objs=[
            Product(
                product=row['product'],
                description=row['description']
            )
            for row in list_of_dict
        ]
        prod=objs[0].product
        check = Product.objects.filter(product=prod).exists()
        print(check)

        if not check:
            msg=Product.objects.bulk_create(objs)
        return redirect('inventory_list')

@login_required
def downloadcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product_template.csv"'

    writer = csv.writer(response)
    writer.writerow(['product', 'description'])

    return response


