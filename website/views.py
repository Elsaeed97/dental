from django.shortcuts import render , redirect 
from .models import Message 
from django.core.mail import send_mail
# Create your views here.
def index(request):
	context = {}
	return render(request, 'index.html' ,context)

def about(request):
	context = {}
	return render(request,'about.html', context)

def services(request):
	return render(request,'services.html')

def pricing(request):
	return render(request,'pricing.html')

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		contact = Message()
		contact.name = name
		contact.email = email
		contact.message = message
		contact.save()
		return redirect('contact')

		send_mail(
			name,
			message,
			email,
			['elsaeedahmed97@gmail.com'],
			fail_silently=False 
			)

	return render(request,'contact.html',)