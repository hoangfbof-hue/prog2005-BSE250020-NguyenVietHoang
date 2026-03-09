arr = list(map(int, input().split()))
tong = 0
print("Các số chẵn:")
for x in arr:
    if x % 2 == 0:
        print(x)
        tong += x

print("Tổng các số chẵn:",tong)