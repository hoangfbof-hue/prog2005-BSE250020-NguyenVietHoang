class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        if 0 <= diem <= 10:
            self.diem = diem
        else:
            print(f"Cảnh báo: Điểm của {ten} không hợp lệ (phải từ 0-10). Đã tạm sét về 0.")
            self.diem = 0

    def display(self):
        """Phương thức in thông tin theo định dạng yêu cầu"""
        print(f"Sinh viên {self.ten} có điểm là {self.diem}")

student_a = Student("A", 10)
student_b = Student("B", 8.5)
print("--- Kết quả hiển thị ---")
student_a.display()
student_b.display()
