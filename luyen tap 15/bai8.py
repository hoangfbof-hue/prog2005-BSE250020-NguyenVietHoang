class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 
    @property
    def price(self):
        """Trả về giá trị của thuộc tính ẩn _price"""
        return self._price
    @price.setter
    def price(self, value):
        """Kiểm tra điều kiện trước khi gán giá trị"""
        if value < 0:
            print(f"Lỗi: Giá sản phẩm '{self.name}' không thể nhỏ hơn 0 (Đang nhập: {value})")
            self._price = 0  
        else:
            self._price = value
p1 = Product("Điện thoại", 500)
print(f"Sản phẩm: {p1.name}, Giá: {p1.price}")
print("\nThử gán giá âm:")
p1.price = -100
print(f"Giá hiện tại của {p1.name}: {p1.price}")
print("\nKhởi tạo sản phẩm với giá âm:")
p2 = Product("Laptop", -50)
