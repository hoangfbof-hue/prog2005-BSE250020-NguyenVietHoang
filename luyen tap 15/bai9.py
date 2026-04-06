def luu_chuoi_vao_file(ten_file="data.txt"):
    noi_dung = input("Nhập chuỗi ký tự bạn muốn lưu: ")

    try:
        with open(ten_file, "w", encoding="utf-8") as f:
            f.write(noi_dung)
        
        print(f"\nThành công! Nội dung đã được lưu vào file: {ten_file}")

    except Exception as e:
        print(f"Đã xảy ra lỗi khi ghi file: {e}")
luu_chuoi_vao_file("ket_qua.txt")
