from django.core.exceptions import ValidationError
import datetime
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.forms import widgets
from django.forms import inlineformset_factory
from django.db import transaction
from django.urls import reverse_lazy
from Inventory.models import *
from .models import Sales, SalesItem
from .forms import *
from django.http import JsonResponse
@login_required
def sales_list(request):
    sales=Sales.objects.all().order_by('-id')
    return render(request,'sales/sales_list.html',{'sales':sales})



class SalesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Sales
    template_name = "sales/sales_form.html"
    fields = '__all__'
    success_message = "New sales successfully added."

    def get_context_data(self, **kwargs):
        data = super(SalesCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = SaleItemFormset(self.request.POST)
        else:
            data['items'] = SaleItemFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        data={}
        with transaction.atomic():
            if items.is_valid():
                items.instance = form.save(commit=False)
                for i in items:
                    prod = i.cleaned_data['product']
                    product=prod.product
                    qt=i.cleaned_data['quantity']
                    sold_item=Product.objects.get(product=product)
                    if qt <= sold_item.Quantity:
                        data[product] = qt
                        print(data)
                        sold_item.Quantity -=qt
                        sold_item.save()
                        form.save()
                        items.save()
                     
                    else:
                        form.errors['VALUE ERROR :: ']='Your entered quantity exceeds inventory quantity'
                        return self.form_invalid(form)
                        
        return super(SalesCreateView, self).form_valid(form)

    def get_initial(self):
        initial=super(SalesCreateView,self).get_initial()
        initial['customer']=Customer.objects.get(pk=self.kwargs['pk'])
        return initial
    #
    # def post(self, request, pk):
    #     # sold_item = Product.objects.get(id=pk)
    #     sales_form = SaleItemFormset(request.POST)
    #     if sales_form.is_valid():
    #         new_sale = sales_form.save(commit=False)
    #         new_sale.save()

    #         # sold_quantity = int(request.POST['quantity'])
    #         # sold_item.Quantity -= sold_quantity
    #         # sold_item.save()
    #         return redirect('sales-list')b265p0lm

class CustomerAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Customer
    template_name = "sales/add_customer.html"
    fields = '__all__'
    success_message = "New Customer successfully added."



def sales_details(request,pk):
    customer_instance = Customer.objects.get(id=pk)
    print(customer_instance)
    # sales_instance = Sales.objects.get(pk = pk)
    sales = customer_instance.sales_set.all().filter(date = datetime.date.today())
    sales_dataset = []
    sales_items = SalesItem.objects.filter(sales_id__customer = customer_instance,sales_id__date = datetime.date.today())
    for sale in sales:
        sale_itm = Sales.objects.filter(pk = sale.id)
        sales_dataset.append({'sale_itm':sale_itm})
    print(sales_dataset)
        
    print(sales_items)
    context = {'sales_items':sales_items,'customer_instance':customer_instance,'sales':sales_dataset}
    return render(request,'sales/sales_detail.html',context)

class SalesDetail(LoginRequiredMixin,DetailView):
    model = Sales
    template_name = 'sales/sales_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SalesDetail, self).get_context_data(**kwargs)
        return context

def SalesUpdateView(request, sales_id):
    sale = Sales.objects.get(id=sales_id)
    form = SaleForm(request.POST, instance=sale)
    ItemFormset = inlineformset_factory(Sales, SalesItem, form=SaleForm, extra=0)

    if request.method == 'POST':
        formset = ItemFormset(request.POST, instance=sale)

        if formset.is_valid():
            form.save()
            formset.save()
            from django.contrib import messages
            messages.success(request, 'Order successfully updated')
            return redirect('sales_details', sales_id)
    else:

        form = SaleForm(instance=sale)
        formset = ItemFormset(instance=sale)

    return render(request, 'sales/sales_update.html', {'form':form, 'sale_object':sale,'formset' : formset})


def sales_return_list(request):
    sales=Sales.objects.all().order_by('-id')
    return render(request,'sales/sales_return_list.html',{'sales':sales})

def existing_customer_list(request):
    sales=Customer.objects.all()
    return render(request,'sales/existing_customer.html',{'sales':sales})

class CustomerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Customer
    template_name = "sales/add_customer.html"
    fields = '__all__'
    success_message = "Record successfully updated."
    success_url = reverse_lazy('customer-list')

    def get_form(self):
        form = super(CustomerUpdateView, self).get_form()
        form.fields['name'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['phone_no'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['email'].widget = widgets.EmailInput(attrs={'rows': 1})

        return form


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = "supplier/supplier_confirm_delete.html"
    success_url = reverse_lazy('customer-list')

class existing_sales_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Sales
    template_name = "sales/sales_form.html"
    fields = '__all__'
    success_message = "New sales successfully added."
    # success_url = reverse_lazy('existing-sales-create', kwargs={'id': 'pk'})
    
    def get_success_url(self):
        customer_id = Customer.objects.get(pk=self.kwargs['pk']).pk
        return reverse('existing-sales-create', kwargs={'pk': customer_id})

    def get_context_data(self, **kwargs):
        data = super(existing_sales_create, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = SaleItemFormset(self.request.POST)
            data['customer'] = Customer.objects.get(pk=self.kwargs['pk'])
        else:
            data['items'] = SaleItemFormset()
            data['customer'] = Customer.objects.get(pk=self.kwargs['pk'])
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            if items.is_valid():
                items.instance = form.save(commit=False)
                for i in items:
                    prod = i.cleaned_data['product']
                    product=prod.product
                    qt=i.cleaned_data['quantity']
                    print(qt)
                    sold_item=Product.objects.get(product=product)
                    print(sold_item.Quantity)
                    if qt <= int(sold_item.Quantity):
                        sold_item.Quantity -= qt
                        sold_item.save()
                        form.save()
                        items.save()
                    else:
                        form.errors['value'] = 'Your entered quantity exceeds inventory quantity'
                        
                        return self.form_invalid(form)
        return super(existing_sales_create, self).form_valid(form)

    def get_initial(self):
        initial = super(existing_sales_create, self).get_initial()
        initial['customer'] = Customer.objects.get(pk=self.kwargs['pk'])
        return initial

class SalesReturnView(LoginRequiredMixin,DetailView,UpdateView):
    model = Sales
    fields='__all__'
    template_name = 'sales/sales_return_update.html'

    def get_context_data(self, **kwargs):
        data = super(SalesReturnView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = SaleItemFormset(self.request.POST)
        else:
            data['items'] = SaleItemFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        name=context['object']
        name_id=Customer.objects.get(name=name)
        sales_id=Sales.objects.filter(customer_id=name_id).first()
        items = context['items']
        with transaction.atomic():
            if items.is_valid():
                items.instance = form.save(commit=False)
                for i in items:
                    prod = i.cleaned_data['product']
                    qt=i.cleaned_data['quantity']
                    product=prod.product
                    sales_item_id = SalesItem.objects.filter(sales_id_id=sales_id, product_id=prod.id)
                    for i in sales_item_id:
                        i.quantity -= qt
                        i.save()
                        sold_item=Product.objects.get(product=product)
                        sold_item.Quantity +=qt
                        sold_item.save()
        return super(SalesReturnView, self).form_valid(form)


def manage_customers(request):
    customers=Customer.objects.all()
    return render(request,'sales/manage_customers.html',{'customers':customers})

# @csrf_exempt
def sales_item_total_price(request):
    item_id = request.GET['item_id']
    print(item_id)
    item_quantity = request.GET['item_quantity']
    
    sales_item_instance = SalesItem.objects.filter(product=item_id).first()
    product_sale_price = sales_item_instance.product.sale_price
    print(product_sale_price,"Sales price::;")
    total_price = int(item_quantity) * float(product_sale_price)
   
    return JsonResponse({'total_price':total_price})
    