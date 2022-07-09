from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
  path('', dashboard, name='home'),

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', include('corecode.urls')),
    # path('student/', include('students.urls')),
    # path('finance/', include('finance.urls')),
    path('inventory/', include('Inventory.urls')),
    path('supplier/', include('supplier.urls')),
    path('sales/', include('sales.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
