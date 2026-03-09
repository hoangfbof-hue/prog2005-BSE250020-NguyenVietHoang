arr = list(map(int, input().split()))
n = len(arr)
sodoi = 0
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            sodoi += 1
print(arr)
print("Số lần hoán đổi:", sodoi)