from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Visitor, Contact

import datetime

# Create your views here.
def index(requests):
	x_forward = requests.META.get('HTTP_X_FORWARDED_FOR')
	if x_forward:
		ip = x_forward.split(',')[0]
	else:
		ip = requests.META.get('REMOTE_ADDR')
	v = Visitor(ip=str(ip), date=str(datetime.datetime.now()))
	v.save()
	if (requests.method == 'POST'):
		data = requests.POST.get("email",False)
		user = User.objects.create_user(username=data.split('@')[0], email=data)
		
	if (requests.method == "GET"):
		name = requests.GET.get("name2", False)
		email = requests.GET.get("email2", False)
		message = requests.GET.get("message2", False)
		c = Contact(name=name, email=email, message=message)
		c.save()
	return render(requests, 'Quant/index.html')
