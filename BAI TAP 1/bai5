import random
try:
    m = int(input("Nhập số hàng (M): "))
    n = int(input("Nhập số cột (N): "))
    matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]
    print("\nMa trận vừa khởi tạo:")
    for row in matrix:
        print(row)
    row_idx = int(input(f"\nNhập số hàng muốn hiển thị (1 đến {m}): "))
    if 1 <= row_idx <= m:
        print(f"Hàng {row_idx}: {matrix[row_idx - 1]}")
    else:
        print("Lỗi: Số hàng không hợp lệ.")
    col_idx = int(input(f"Nhập số cột muốn hiển thị (1 đến {n}): "))
    if 1 <= col_idx <= n:
        column_data = [matrix[i][col_idx - 1] for i in range(m)]
        print(f"Cột {col_idx}: {column_data}")
    else:
        print("Lỗi: Số cột không hợp lệ.")
    max_val = max(max(row) for row in matrix)
    print(f"\nGiá trị lớn nhất trong ma trận là: {max_val}")

except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
