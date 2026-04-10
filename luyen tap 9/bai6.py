class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Giá phải lớn hơn 0!")

    def __str__(self):
        return f"Product Price: {self._price}"

p = Product(500)
print(p)
p.price = 600
print(f"Giá mới: {p.price}")
