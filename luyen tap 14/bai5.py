class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price
danh_sach_sach = [
    Book("Book 1", 30000),
    Book("Book 2", 50000),
    Book("Book 3", 100000)
]
tong_tien = 900000 
file_path = "books.txt"

try:
    with open(file_path, mode="w", encoding="utf-8") as f:
        for b in danh_sach_sach:
            f.write(f"{b.name};{b.price}\n")
      
        f.write(f"Tong;{tong_tien}")
    
    print(f"Đã lưu dữ liệu vào file '{file_path}' thành công!")

except IOError as e:
    print(f"Có lỗi khi ghi file: {e}")
