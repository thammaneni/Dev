from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
	#return HttpResponse('<H1>Hello World</H1>')
	return render(request, 'home.html',{})
	
	
	
def contact_view(*args,**kwargs):
	return HttpResponse('<H1>Contact info</H1>')