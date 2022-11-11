# Instatiate Django and import settings
import os
#mark django settings module as settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

#instantiate a web sv for django which is a wsgi
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#import your models schema
from MyApp.models import Person

#Create Operations here
data_dict={'name':'Banana','codes':1,price:0.99}
data_dict={'name':'Apple','codes':2,price:0.79}
data_dict={'name':'Milk','codes':3,price:3.99}
data_dict={'name':'Flour','codes':4,price:2.49}
product = Product(**data_dict)
product.save()

# Read operation logic
product = Product.objects.get()

print(f'Product Name: {product.name}, Product code: {product.codes} Price: ${product.price}')
#Prints Hello, I am Nimish, 23 y/o. Reachable at nimishverma@ymail.com