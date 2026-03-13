import math

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


input_str = input("Nhập chuỗi các số (cách nhau bằng dấu chấm phẩy ';'): ")
danh_sach_str = input_str.split(';')
danh_sach_so = [int(s.strip()) for s in danh_sach_str if s.strip()]
so_chan = 0
so_am = 0
so_nguyen_to = 0
tong = 0

print("\n--- KẾT QUẢ XỬ LÝ ---")
print("Danh sách từng số:")
for n in danh_sach_so:
    print(n)
    tong += n
    if n % 2 == 0:
        so_chan += 1
    if n < 0:
        so_am += 1
    if la_so_nguyen_to(n):
        so_nguyen_to += 1
trung_binh = tong / len(danh_sach_so) if danh_sach_so else 0
print("-" * 20)
print(f"Số lượng số chẵn: {so_chan}")
print(f"Số lượng số âm: {so_am}")
print(f"Số lượng số nguyên tố: {so_nguyen_to}")
print(f"Giá trị trung bình: {trung_binh:.2f}")
