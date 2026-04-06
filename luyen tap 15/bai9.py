def luu_file():
    chuoi_nhap = input("Nhập chuỗi ký tự: ")
    f = open("data.txt", "a", encoding="utf-8")
    
    try:
        print(chuoi_nhap, file=f)
        print("Đã lưu dữ liệu thành công.")
    finally:
        f.close()
        print("File đã được đóng.")
luu_file()
