try:
    toan = float(input("Nhập điểm môn Toán: "))
    van = float(input("Nhập điểm môn Văn: "))
    anh = float(input("Nhập điểm môn Anh: "))
    if any(diem < 0 or diem > 10 for diem in [toan, van, anh]):
        print("Lỗi: Điểm số phải nằm trong khoảng từ 0 đến 10.")
    else:
        dtb = (toan + van + anh) / 3
        if dtb >= 8.0:
            xep_loai = "Giỏi"
        elif dtb >= 6.5:
            xep_loai = "Khá"
        elif dtb >= 5.0:
            xep_loai = "Trung bình"
        else:
            xep_loai = "Yếu"
        print("-" * 30)
        print(f"Điểm trung bình: {dtb:.2f}")
        print(f"Xếp loại: {xep_loai}")

except ValueError:
    print("Lỗi: Vui lòng nhập số điểm hợp lệ!")
