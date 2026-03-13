diem = float(input("Nhập điểm sinh viên (0-10): "))

if 0 <= diem <= 10:
    print(f"Điểm {diem} hợp lệ.")
else:
    print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10.")
