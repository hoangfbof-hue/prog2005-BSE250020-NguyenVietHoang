n = input("Nhập một số: ")
tong = sum(int(chu_so) for chu_so in n if chu_so.isdigit())

print(f"Tổng các chữ số của {n} là: {tong}")
