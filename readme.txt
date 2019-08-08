setup project directory for Django
----------------------------------
=>Create Parent directory workspace
mkdir Dev

cd Dev
=>Create Virualenv dir
mkdir trydjango
cd trydjango

=>create virualenv in trydjango dir
virtualenv .

=>activate virtualenv
Scripts\activate

=>To see installed versions on virtualenv
pip freeze

=>To see available command lists in virtualenv
django-admin
0utput:
Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
=>django-admin startproject trydjango .

=>python manage.py runserver

settings.py
===========
stuff like that


=>python manage.py migrate
to make all changes saved/migrated.

Createsuperuser for admin module:
--------------------------------
python manage.py createsuperuser

username: thamma
pwd: thamma123

Create new-App:
---------------
python manage.py startapp products

Connecting to shell:
-------------------
=>python manage.py shell

=>from products.models import Product

=>Product.objects.all()

=>Product.objects.create(title='Title of product',description='description of products',price='1235',summary='Summary of products')

we can add no.of products into database.

Customising model Product:
-------------------------

	title			= models.CharField(max_length=100)
	description 	= models.TextField(blank=True, null=True)
	price 			= models.DecimalField(decimal_places=2, max_digits=1000)
	summary			= models.TextField(blank=False)
	features		= models.BooleanField()
	
	
Here, blank=True referes optional Field, no need to enter any value.
if blank is False, it is mandatory Field.

for all changes you need to run:
python manage.py makemigrations
python manage.py migrate

----------------------------
Creating basic views.

python manage.py startapp pages

views.py:
--------
def home_view(request,*args,**kwargs):
	#return HttpResponse('<H1>Hello World</H1>')
	return render(request, 'home.html',{})

here request is URL page request object and arguments are passed by user request page, {} context dict represents users input parameters

added all views and create template directory and create html files for each view.

Template Inheritance:
--------------------

base.html - is the one to having proto type of all backgroud html views

we have to user tags to extends base.html file to all other html files.

{% extends 'base.html' %}

{% block content %}
your customized template goes here 
{% endblock %}
====================

include html pages:
------------------
We can define short html pages and import them in several pages

navbar.html - contains only navbar options

to include navbar.html we have to use {% include 'navbar.html' %}

Rendering context into HTML pages:
---------------------------------
In case of sending date from view functions to html pages, need to define dict variable(Recomended) or normal variable and pass it in reder function


def about_view(request, *args, **kwargs):
    my_context={
        'title':"This is Context variable of about page",
        'price': 2365.25,
        'name': 'Soap'
    }
    return render(request, 'about.html', my_context)


call variables in HTML files as :

{% block content %}
<h2> This is About page </h2>
{{ title }} </br>
{{ price }}</br>
{{ name }}</br>

{% endblock %}

for loop:
--------
<ul>
{% for item in my_list %}
    <li> {{ forloop.counter}} - {{ item }}</li>
{% endfor %}

conditioning in templates:
{% if name == 'Soap' %}
    <H1>Name is Soap</H1>
{% else %}
    <h2> undefined </h2>
{% endif %}


for more Built in template tags and filters:
https://docs.djangoproject.com/en/2.2/ref/templates/builtins/



























