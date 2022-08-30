from django.urls import path
from .views import *

urlpatterns=[
path('',sales_list,name='sales-list'),
path('customers/index/',manage_customers,name='customer-list'),
  path('<pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
path('<pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
path('create-customer/', CustomerAddView.as_view(), name='create-customer'),
path('sale-detail/<int:pk>',sales_details, name='sales_details'),
path('sales-detail/<int:pk>',sales_details_from_report, name='sales_details_from_report'),

path('<int:sales_id>/update/', SalesUpdateView, name='sales-update'),
path('return/',view_customer_return,name='sales-return-list'),
path('return/<pk>/',return_customer_each_sales,name='return-customer-sale'),
path('existing/',existing_customer_list,name='existing-customer-list'),
path('create/<int:pk>',SalesCreateView.as_view(),name='sales-create'),

path('exist/create/<int:pk>',existing_sales_create.as_view(),name='existing-sales-create'),
path('<int:pk>/return/',SalesReturnView.as_view(),name='sales-return'),

path('get-total-stock/',get_total_stock,name='get-total-stock'),
path('sales-item-total-price/',sales_item_total_price,name='sales-item-total-price'),
path('return-product-list/',product_return_list,name='return-product-list'),


]