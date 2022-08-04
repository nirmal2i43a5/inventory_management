from django.urls import path
from .views import *

urlpatterns=[
path('',sales_list,name='sales-list'),
path('customers/index/',manage_customers,name='customer-list'),
  path('<pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
path('<pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
path('create/<int:pk>',SalesCreateView.as_view(),name='sales-create'),
path('create-customer/', CustomerAddView.as_view(), name='create-customer'),
path('sale-detail/<int:pk>',sales_details, name='sales_details'),
path('<int:sales_id>/update/', SalesUpdateView, name='sales-update'),
path('return/',sales_return_list,name='sales-return-list'),
path('existing/',existing_customer_list,name='existing-customer-list'),
path('exist/create/<int:pk>',existing_sales_create.as_view(),name='existing-sales-create'),
path('<int:pk>/return/',SalesReturnView.as_view(),name='sales-return'),

path('sales-item-total-price/',sales_item_total_price,name='sales-item-total-price'),


]