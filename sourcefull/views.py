from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.urls import reverse



import requests

# Create your views here.
    	


def index(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')

		data = {
			'name': name,
			'email': email,
			'subject': subject,
			'message': message
		}
		print(data)
	return render(request, 'index.html', {})


def webdesign(request):
    return render(request, 'webdesign.html')


    
