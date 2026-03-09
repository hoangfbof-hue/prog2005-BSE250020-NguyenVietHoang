arr = list(map(int, input().split()))
for x in arr:
    if x > 10:
        print("Số đầu tiên > 10 là:", x)
        break
else:
    print("Không có số nào > 10")