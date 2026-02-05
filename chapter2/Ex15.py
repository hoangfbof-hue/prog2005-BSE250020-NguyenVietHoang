try:
    n = int(input("Nhập vào một số nguyên dương: "))
    
    if n < 0:
        print("Vui lòng nhập số dương!")
    else:
        so_ban_dau = n
        tong = 0
        while n > 0:
            chu_so = n % 10 
            tong += chu_so  
            n = n // 10     
        print(f"Tổng các chữ số của {so_ban_dau} là: {tong}")

except ValueError:
    print("Lỗi! Bạn phải nhập vào một số nguyên.")
