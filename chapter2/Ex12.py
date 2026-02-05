try:
    n = int(input("Nhập vào số nguyên dương n: "))

    if n < 1:
        print("Vui lòng nhập n >= 1.")
    else:
        tong_le = 0
        for i in range(1, n + 1, 2):
            tong_le += i
        
        print(f"Tổng các số lẻ từ 1 đến {n} là: {tong_le}")

except ValueError:
    print("Lỗi! Vui lòng nhập một số nguyên.")
