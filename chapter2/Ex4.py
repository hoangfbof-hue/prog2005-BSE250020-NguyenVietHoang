num_str = input("Nhập một số nguyên: ")
tong = sum(int(ky_tu) for ky_tu in num_str if ky_tu.isdigit())

print(f"Tổng các chữ số là: {tong}")
