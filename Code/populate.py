from cash_register.models import Product
p = Product(name= "Coke", code= 1114, price= 1.5)
p.save()
p = Product(name="Oranges", code=1115, price= 0.62)
p.save()
p = Product(name="Cookies", code=1116, price= 2.2)
p.save()
