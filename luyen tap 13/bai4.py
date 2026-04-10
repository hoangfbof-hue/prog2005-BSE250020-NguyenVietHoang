def tinh_tong_de_quy(n):
    if n == 1:
        return 1
    return n + tinh_tong_de_quy(n - 1)

n = int(input("Nhập n: "))
if n > 0:
    print(f"Tổng từ 1 đến {n} là: {tinh_tong_de_quy(n)}")
else:
    print("Vui lòng nhập n > 0")
