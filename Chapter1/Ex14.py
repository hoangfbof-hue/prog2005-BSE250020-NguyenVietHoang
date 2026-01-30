import math

try:
    number = float(input("Nhập một số để tính căn bậc hai: "))
    if number < 0:
        print("Lỗi: Không thể tính căn bậc hai của một số âm trong tập số thực.")
    else:
        square_root = math.sqrt(number)
        print(f"Căn bậc hai của {number} là: {square_root:.4f}")

except ValueError:
    print("Lỗi: Vui lòng nhập một con số hợp lệ.")
