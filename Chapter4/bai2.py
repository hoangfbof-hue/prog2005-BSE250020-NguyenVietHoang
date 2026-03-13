def tinh_diem_trung_binh(danh_sach_sinh_vien):
    """
    Hàm nhận vào một dictionary và trả về điểm trung bình.
    """
    if not danh_sach_sinh_vien:
        return 0

    danh_sach_diem = danh_sach_sinh_vien.values()

    tong_diem = sum(danh_sach_diem)
    so_luong = len(danh_sach_sinh_vien)

    trung_binh = tong_diem / so_luong
    return trung_binh


sinh_vien_dict = {
    "Nguyễn Văn Anh": 8.5,
    "Trần Thị Bi": 9.0,
    "Lê Văn Can": 7.5,
    "Phạm Minh Dinh": 10.0
}

dtb = tinh_diem_trung_binh(sinh_vien_dict)
print("--- Danh sách sinh viên và điểm ---")
for ten, diem in sinh_vien_dict.items():
    print(f"- {ten}: {diem}")

print("-" * 35)
print(f"Điểm trung bình của {len(sinh_vien_dict)} sinh viên là: {dtb:.2f}")
