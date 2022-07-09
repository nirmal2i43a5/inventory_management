from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
  path('dashboard/', dashboard, name='home'),
  path('', front_page, name='front_page'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    	path('authentication/',include('registers.urls', namespace = 'register_app')),
    # path('', include('corecode.urls')),
    # path('student/', include('students.urls')),
    # path('finance/', include('finance.urls')),
    path('inventory/', include('Inventory.urls')),
    path('supplier/', include('supplier.urls')),
    path('sales/', include('sales.urls')),
    
	path('reset_password/',auth_views.PasswordResetView.as_view(template_name = 'passwordreset/password_reset_email.html'), 
		 name = "password_reset"),
	
	path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name = 'passwordreset/password_reset_sent.html'), 
		 name = "password_reset_done"),
	
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='passwordreset/password_reset_form.html'),
		 name="password_reset_confirm"),  
	   
	 #<token> check  for valid user or not--><uidb64> user id encoded in base 64--this email is sent to the user
	 #<uidb64> helps to know user who request for password
	path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='passwordreset/password_reset_complete.html'),
		 name="password_reset_complete"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
