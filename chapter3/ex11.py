arr = list(map(int, input().split()))
maxx = arr[0]
minn = arr[0]

for x in arr:
    if x > maxx:
        maxx = x
    if x < minn:
        minn = x

print("Giá trị lớn nhất:", maxx)
print("Giá trị nhỏ nhất:", minn)