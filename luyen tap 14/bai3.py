import math

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
try:
    input_str = input("Nhập các số tự nhiên (ngăn cách bởi dấu cách): ")
    mang = [int(x) for x in input_str.split()]
    so_le = [x for x in mang if x % 2 != 0]
    print(f"Số lẻ: {' '.join(map(str, so_le))} | Tổng số lượng số lẻ: {len(so_le)}")
    so_nt = [x for x in mang if la_so_nguyen_to(x)]
    print(f"Số nguyên tố: {' '.join(map(str, so_nt))}")

except ValueError:
    print("Vui lòng chỉ nhập các số tự nhiên!")
