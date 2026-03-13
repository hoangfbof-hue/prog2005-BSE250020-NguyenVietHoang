class Hoa:
    def __init__(self, ten, mau):
        """Khởi tạo thuộc tính Tên và Màu cho hoa"""
        self.ten = ten
        self.mau = mau

    def __str__(self):
        """Định nghĩa định dạng hiển thị khi gọi hàm print()"""
        return f"Hoa {self.ten} có màu {self.mau}"

hoa_cua_toi = Hoa("Hồng", "Đỏ")

print(hoa_cua_toi)
