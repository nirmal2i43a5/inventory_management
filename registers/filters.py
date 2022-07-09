import django_filters
from django_filters import DateFilter, CharFilter

from customers.models import Customer
from django.forms.widgets import TextInput


class CustomerFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte',label="",
                         widget=TextInput(attrs={'placeholder': ' Data >  =   (YYYY-MM-DD)'}))

	end_date = DateFilter(field_name="date_created", lookup_expr='lte',label="",widget=TextInput(attrs={'placeholder': ' Data <  =  (YYYY-MM-DD)'}))
	# note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ('date_created','email','name','contact',)
  


	