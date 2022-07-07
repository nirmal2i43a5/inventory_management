from django.urls import path

from .views import inventory_list, ProductDeleteView, ProductDetailView, ProductUpdateView, ProductCreateView, ProductBulkUploadView,downloadcsv

urlpatterns = [
  path('product/list/', inventory_list, name='inventory_list'),
  path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
  path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
  path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),

  path('create/', ProductCreateView.as_view(), name='product-create'),
  path('upload/', ProductBulkUploadView.as_view(), name='product-upload'),
  path('downloadcsv/', downloadcsv, name='download-csv'),

]
