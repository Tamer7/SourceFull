from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import time

from django.urls import reverse


from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy



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

def translations(request):
    return render(request, 'translations.html')

def advertisement(request):
    return render(request, 'advertisement.html')
    	




class ContactView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')


    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'success.html'



    
