from django.urls import path
from .views import *
urlpatterns=[
    path('list',supplier_list, name='supplier-list'),
    path('create/', SupplierCreateView.as_view(), name='supplier-create'),
    path('<uuid:pk>/update/', SupplierUpdateView.as_view(), name='supplier-update'),
    path('<uuid:pk>/delete/', SupplierDeleteView.as_view(), name='supplier-delete'),
    path('<uuid:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),

]