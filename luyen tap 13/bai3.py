i = 1
tong = 0

print("Các số lẻ từ 1 đến 30 là:")
while i <= 30:
    if i % 2 != 0:
        print(i, end=" ")
        tong += i
    i += 1

print(f"\nTổng của các số lẻ này là: {tong}")
