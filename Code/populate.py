from cash_register.models import Product
p = Product(name: "Banana", code: 1111, price: 1.2)
p.save()
p = Product(name="Apple", code=1112, price=0.89)
p.save()
p = Product(name="Milk", code=1113, price=3.4)
p.save()
