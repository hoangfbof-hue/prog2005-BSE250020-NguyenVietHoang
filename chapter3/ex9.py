arr = list(map(int, input().split()))
print("Các số lẻ:")
for x in arr:
    if x % 2 != 0:
        print(x)