n = int(input("Nhập một số nguyên: "))

if n < 0:
    print("Lỗi: Số nhập vào không được là số âm.")
else:
    du = n % 2
    print(f"Phần dư của {n} khi chia cho 2 là: {du}")
