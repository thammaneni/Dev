from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.

def product_create_view(request):
	my_form = ProductForm()

	if request.method == 'POST':
		my_form = ProductForm(request.POST)

		if my_form.is_valid():
			print(my_form.cleaned_data)
			Product.objects.create(**my_form.cleaned_data)
			print(request.POST)
	context = {
		'form' : my_form
	}
	return render(request, 'products/product_create_form.html', context)



def product_detail_view(request):
	obj= Product.objects.get(id=1)
	context={
	'object': obj,
	}
	return render(request,'products/product_details.html', context)

def product_view(request):
	print(request.POST)
	return render(request,'products/product_details.html',{})