from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.urls import reverse



import requests

# Create your views here.
def index(request):
	return render(request, 'index.html')
