danh_sach_diem = {
    "Nguyễn Việt Hoàng": 8.5,
    "Trần Thị Bình": 7.0,
    "Lê Văn Cường": 9.0,
    "Phạm Minh Đức": 6.5,
    "Hoàng Thị Hoa": 10.0
}
def tinh_diem_trung_binh(dic_sinh_vien):
    if not dic_sinh_vien:
        return 0
    tat_ca_diem = dic_sinh_vien.values()
    tong_diem = sum(tat_ca_diem)
    so_luong = len(dic_sinh_vien)
    
    trung_binh = tong_diem / so_luong
    return trung_binh
dtb_lop = tinh_diem_trung_binh(danh_sach_diem)

print(f"Danh sách sinh viên và điểm: {danh_sach_diem}")
print("-" * 40)
print(f"Số lượng sinh viên: {len(danh_sach_diem)}")
print(f"Điểm trung bình của cả lớp là: {dtb_lop:.2f}")
