m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
print("Nhập ma trận A:")
A = []
for i in range(m):
    A.append(list(map(int, input().split())))
print("Nhập ma trận B:")
B = []
for i in range(m):
    B.append(list(map(int, input().split())))
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Ma trận tổng:")
for row in C:
    print(row)