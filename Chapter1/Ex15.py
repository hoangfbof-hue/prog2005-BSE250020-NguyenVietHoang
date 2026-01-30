danh_sach_sinh_vien = []
for i in range(1, 4):
    print(f"\n--- Nhập thông tin sinh viên thứ {i} ---")
    ten = input("Nhập tên sinh viên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    diem_tb = (toan + ly + hoa) / 3
    sinh_vien = {
        "ten": ten,
        "diem_tb": diem_tb
    }
    danh_sach_sinh_vien.append(sinh_vien)
print("\n" + "="*30)
print("KẾT QUẢ ĐIỂM TRUNG BÌNH")
print("="*30)

for sv in danh_sach_sinh_vien:
    print(f"Sinh viên: {sv['ten']:<15} | ĐTB: {sv['diem_tb']:.2f}")
