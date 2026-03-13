class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        """Getter: Trả về giá trị của thuộc tính ẩn _price"""
        return self._price

    @price.setter
    def price(self, value):
        """Setter: Kiểm tra điều kiện giá > 0 trước khi gán"""
        if value > 0:
            self._price = value
        else:
            print(f"Lỗi: Giá của '{self.name}' phải lớn hơn 0! (Đang cố gán: {value})")
            self._price = 1.0  # Gán giá trị mặc định tối thiểu nếu lỗi

    def __str__(self):
        """Định nghĩa cách in thông tin đối tượng"""
        return f"Sản phẩm: {self.name} | Giá: {self._price}"
p1 = Product("Laptop", 1500)
print(p1)
p2 = Product("Chuột máy tính", -50)
print(p2)
p1.price = 2000
print(f"Giá mới của {p1.name}: {p1.price}")

p1.price = -10
