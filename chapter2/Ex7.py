try:
    a = int(input("Nhập số nguyên dương thứ nhất: "))
    b = int(input("Nhập số nguyên dương thứ hai: "))

    if a <= 0 or b <= 0:
        print("Vui lòng nhập các số nguyên dương!")
    else:
        so_a, so_b = a, b
      
        while b != 0:
            so_du = a % b
            a = b      
            b = so_du 
        print(f"Ước số chung lớn nhất của {so_a} và {so_b} là: {a}")

except ValueError:
    print("Lỗi! Bạn phải nhập vào số nguyên.")
