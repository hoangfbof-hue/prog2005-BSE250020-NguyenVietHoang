danh_sach_mau = ["Đỏ", "Xanh dương", "Vàng", "Xanh lá", "Tím"]
print("Danh sách ban đầu:", danh_sach_mau)
mau_can_xoa = "Vàng"
if mau_can_xoa in danh_sach_mau:
    danh_sach_mau.remove(mau_can_xoa)
    print(f"Đã xóa màu '{mau_can_xoa}' thành công.")
else:
    print(f"Màu '{mau_can_xoa}' không có trong danh sách.")
print("Danh sách hiện tại:", danh_sach_mau)
