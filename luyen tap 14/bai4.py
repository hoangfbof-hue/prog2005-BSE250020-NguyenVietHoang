class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            print("Giá không thể âm!")
        else:
            self._price = value
my_book = Book("Lập trình Python", 150000)
print(f"Tên sách: {my_book.name}")
print(f"Giá sách: {my_book.price}")
my_book.price = 180000
print(f"Giá sách sau khi cập nhật: {my_book.price}")
