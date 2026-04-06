try:
    so_nhap_vao = int(input("Nhập một số nguyên: "))
    if so_nhap_vao < 0:
        print("Lỗi: Vui lòng nhập một số không âm (>= 0).")
    else:
        phan_du = so_nhap_vao % 2
        print(f"Phần dư của {so_nhap_vao} khi chia cho 2 là: {phan_du}")
        if phan_du == 0:
            print("Đây là số chẵn.")
        else:
            print("Đây là số lẻ.")

except ValueError:
    print("Lỗi: Dữ liệu nhập vào phải là một số nguyên.")
