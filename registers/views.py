from django.shortcuts import render,reverse,redirect,resolve_url

# from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.views.generic import CreateView
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.http import HttpResponse, HttpResponseRedirect
import json

from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# from datetime import datetime
# from django.utils.timezone import datetime
from datetime import datetime, timedelta





def first_page(request):
	current_date = datetime.now()
	return render(request,'registers/firstpage.html',{'current_date':current_date})



#Login views
@unauthenticated_user
def loginPage(request):
	form = LoginForm()
	# form = LoginForm(reequest.POST or None)

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		email =request.POST.get('email')
		user = authenticate(request,email=email, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Username OR password is incorrect')

	context = {'form':form}
	return render(request, 'registers/login.html', context)



#Usersignup views
@unauthenticated_user
def SignupView(request):

	form = SignupForm()
 
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')#retrieving username from save data from form

			group = Group.objects.get(name='employee')#any time a user signup it is associated with employee group directly
			user.groups.add(group)
			print("--------------",user)

			messages.success(request, 'Account was created for ' + username)

			return redirect('register_app:login')
		

	context = {'form':form}
	return render(request, 'registers/register.html', context)


#User logout views
class UserLogout(LogoutView):
	'''
	I use LOGOUT_REDIRECT_URL in setting.py so,when i logout then setting ma set garako url ma janxa for logout
	LOGOUT_REDIRECT_URL = '/user/login/
	'''
	# template_name = 'logout.html'
	pass







































# def employeeProfile(request):
#     return render(request,'registers/user_view.html')


# @admin_only
# def adminProfile(request):
#     return render(request,'registers/admin_view.html')


	
# # from django.contrib.auth.mixins import LoginRequiredMixin

# # @allowed_users(allowed_roles=['admin'])
# @login_required(login_url='/user/login/')
# @admin_only
# def dashboard(request):
# 	# customer = Customer.objects.get(pk=cid)
# 	customers=Customer.objects.all()
# 	total_customers=customers.count()
# 	orders=Order.objects.all()

# 	total_orders=orders.count()
# 	products = Product.objects.all()
# 	total_products = products.count()	
# 	pending=orders.filter(status='Pending').count()#filter la choose(search)  garxa and all pending lai count garxa
# 	delivered=orders.filter(status="Delivered").count()
 
 
# 	myFilter = CustomerFilter(request.GET, queryset=customers)
# 	customers = myFilter.qs #in jinja this customers goes

# 	# today_date = datetime.today()#filter every day order product for daily expenses	

# 	# today_customers = customers.filter(date_created__year = today_date.year,date_created__month = today_date.month,
#     #                                 date_created__day = today_date.day).count()
    
# 	today_customers = customers.filter(date_created__gte = datetime.now() - timedelta(days=1)).count()#details of last 24 hours#b4 i also get same output using above line but now not so use this concept
 
																									
	
# 	# today_order = orders.filter(created_at__year = today_date.year,created_at__month = today_date.month,created_at__day = today_date.day)
# 	today_order = orders.filter(created_at__gte = datetime.now() - timedelta(days=1))

# 	order_total_price=0.00
# 	for order in today_order:
# 		per_total_price = float(order.product.price) * order.quantity
		
# 		order_total_price += per_total_price
  
# 	print(order_total_price)
# 	# customer = Customer.objects.get(pk=cid) #but i need pk = cid(update)
# 	# particular_customer_price=0.00
# 	# for order in customer.order_set.all():
# 	# 	per_total_price = float(order.product.price) * order.quantity
# 	# 	particular_customer_price += per_total_price 
# 	context={
# 			'customers':customers,'orders_total_price':order_total_price,'total_orders':total_orders,
#    			'myFilter':myFilter,'today_customers':today_customers,'current_data':datetime.now(),
# 			'orders_pending':pending,'orders_delivered':delivered,'total_products':total_products,'total_customers':total_customers
# 			}
	
# 	return render(request,'registers/index.html',context)




	
	
	


