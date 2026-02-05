def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * tinh_giai_thua(n - 1)
try:
    so = int(input("Nhập một số nguyên không âm: "))
    
    if so < 0:
        print("Vui lòng nhập số dương!")
    else:
        ket_qua = tinh_giai_thua(so)
        print(f"Giai thừa của {so} ({so}!) là: {ket_qua}")
        
except ValueError:
    print("Lỗi! Bạn phải nhập vào một số nguyên.")
