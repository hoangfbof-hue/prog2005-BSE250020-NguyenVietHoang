s = input("Nhập chuỗi: ")
u=s[::-1]
rev = ""
for char in s:
    rev = char + rev
print("Chuỗi đảo ngược:", rev,u)