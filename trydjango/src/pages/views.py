from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
	#return HttpResponse('<H1>Hello World</H1>')
	return render(request, 'home.html',{})
	
def about_view(request, *args, **kwargs):
	my_context={
		'title':"this is Context variable of about page",
		'price': 2365.25,
		'name': 'Soap',
		'msg':'<h1> This is HTML format text </h1>'
	}
	return render(request, 'about.html', my_context)
	
	
def contact_view(request, *args, **kwargs):
	return render(request, 'contact.html', {})


