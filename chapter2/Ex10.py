def tinh_tong_de_quy(n):
    if n == 1:
        return 1
    else:
        return n + tinh_tong_de_quy(n - 1)
try:
    n = int(input("Nhập vào một số nguyên dương n: "))

    if n <= 0:
        print("Vui lòng nhập một số lớn hơn 0!")
    else:
        ket_qua = tinh_tong_de_quy(n)
        print(f"Tổng các số từ 1 đến {n} là: {ket_qua}")

except ValueError:
    print("Lỗi! Bạn phải nhập vào một số nguyên.")
except RecursionError:
    print("Số quá lớn vượt quá khả năng xử lý đệ quy của hệ thống!")
