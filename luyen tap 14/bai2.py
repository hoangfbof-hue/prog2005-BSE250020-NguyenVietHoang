danh_sach_ten = []
print("Nhập tên của 5 người:")
for i in range(5):
    ten = input(f"Nhập tên người thứ {i+1}: ")
    danh_sach_ten.append(ten)
print("\nDanh sách sau khi nhập:", danh_sach_ten)
if len(danh_sach_ten) >= 2:
    ten_bi_xoa = danh_sach_ten.pop(1)
    print(f"\nĐã xóa người ở vị trí thứ hai: {ten_bi_xoa}")
print("Danh sách cuối cùng:", danh_sach_ten)
