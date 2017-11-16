from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Users
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
	context = {}
	if request.session['username']:
 		name = request.session['username']

	return render(request,'store/index.html', context)

def signin(request):
	return render(request,'store/signin.html')

def loggedin(request):
	context = {}
	if request.method == 'POST':
		email=request.POST['email']
		try:
			checkemail = Users.objects.get(email=email)
		except Users.DoesNotExist:
			checkemail = None
		if checkemail is not None:
			pwd = request.POST['pwd']
			passwordcheck = Users.objects.get(email=email)
			if pwd == passwordcheck.password:
				request.session['username'] = email
				request.session['password'] = pwd
				test = request.session['username']
				context={'name':test}
				return render(request,'store/loggedin.html',context)
			else:
				context['log'] = "Email and password do not match, please make sure you have entered the correct password"
		else:
			context['log'] = "Email account has not been registered"
	return render(request, 'store/signin.html',context)

def signup(request):
	context = {}
	if request.method == 'POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		phone=request.POST['phone']
		address=request.POST['address']
		postcode=request.POST['postcode']
		email=request.POST['email']
		pwd=request.POST['pwd']	

		store_query =Users(fname = fname, lname = lname, email = email, phone=phone, address_line=address, postcode=postcode, password=pwd)
		store_query.save()


	return render(request, 'store/signin.html', {'register':"You have successfully registered!"})	