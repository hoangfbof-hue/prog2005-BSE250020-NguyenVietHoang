def nhap_ma_tran(ten, r, c):
    matrix = []
    for i in range(r):
        row = []
        for j in range(c):
            val = input(f"Nhập {ten}[{i}][{j}]: ")
            if val.strip() == "":
                raise ValueError("Lỗi: Giá trị nhập vào không được để trống!")
            row.append(float(val))
        matrix.append(row)
    return matrix

try:
    rows = int(input("Nhập số hàng: "))
    cols = int(input("Nhập số cột: "))

    print("Nhập ma trận A:")
    A = nhap_ma_tran("A", rows, cols)
    print("Nhập ma trận B:")
    B = nhap_ma_tran("B", rows, cols)
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

    print("\nKết quả ma trận A + B:")
    for r in result:
        print(r)
except ValueError as e:
    print(e)
