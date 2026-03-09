arr = list(map(int, input().split()))
x = int(input())
for i in range(len(arr)):
    if arr[i] == x:
        print("Tìm thấy tại vị trí:", i)
        break
else:
    print("Không tìm thấy")