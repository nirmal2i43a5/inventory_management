from django.db import models

# Create your models here.
from django.contrib.auth.models import User#for profile i need User

from django.dispatch import receiver
from django.db.models.signals import post_save#user object  signal create hunxa




class Profile(models.Model):#THis is employee profile
	#in django username [assword1 and password2 are default field --but we make this model if we want to add extra field]
 
	user = models.OneToOneField(User, on_delete=models.CASCADE)#one user have one user nad pw so onetoone field
 
	fname = models.CharField(max_length=100,null=True)#null true means use value when needed
	lname = models.CharField(max_length=100,null=True)
	address = models.CharField(max_length=100, null=True)
	contact = models.CharField(max_length=100,null =True)
	email=models.EmailField(max_length=100,null=True)
	# profile_img = models.ImageField(null=True, blank=True)
 
	def __str__(self):
		return self.user.username    #i use this function because i dont use null =True in user -everytime i need this
	
	
	class Meta:
		verbose_name_plural ='Profile'
		db_table = 'tbl_profile'

		
		
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
  
  

		
		
	
	
	@receiver(post_save, sender = User)#post save paxi uend by user--for register
	def update_profile(sender,instance,created,*args,**kwargs):
		if created:
			Profile.objects.create(user=instance)
			instance.profile.save()
			
			
			
			

