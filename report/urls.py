from django.urls import path
from .views import *
urlpatterns=[
    path('customers/',view_customer_report, name='customers_report'),
        path('customer/sale-report/<str:id>/',each_customer_sales_report, name='each-sales-report'),
          path('product/',product_report, name='product_report'),


]