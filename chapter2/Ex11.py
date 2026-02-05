try:
    diem = float(input("Nhập điểm trung bình của học sinh: "))
    if diem < 0 or diem > 10:
        print("Điểm không hợp lệ! Vui lòng nhập trong khoảng từ 0 đến 10.")
    else:
        if diem >= 8.0:
            xep_loai = "Giỏi"
        elif diem >= 6.5:
            xep_loai = "Khá"
        elif diem >= 5.0:
            xep_loai = "Trung bình"
        else:
            xep_loai = "Yếu"
        print(f"Với số điểm {diem}, xếp loại của học sinh là: {xep_loai}")

except ValueError:
    print("Lỗi! Vui lòng nhập vào một con số (ví dụ: 7.5).")
