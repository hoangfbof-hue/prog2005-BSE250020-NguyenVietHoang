def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
try:
    so_nhap = int(input("Nhập một số nguyên dương: "))

    if so_nhap < 0:
        print("Vui lòng nhập số không âm.")
    else:
        ket_qua = tinh_giai_thua(so_nhap)
        print(f"Giai thừa của {so_nhap} là: {ket_qua}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")
