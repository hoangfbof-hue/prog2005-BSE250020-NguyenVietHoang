import csv

ten_nv = input("Tên nhân viên: ")
tuoi_nv = input("Tuổi: ")
id_nv = input("ID: ")

with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"ID: {id_nv}, Tên: {ten_nv}, Tuổi: {tuoi_nv}")

with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Tên", "Tuổi"])
    writer.writerow([id_nv, ten_nv, tuoi_nv])

print("Đã lưu thông tin vào file nhanvien.txt và nhanvien.csv.")
print("\n--- Nội dung file vừa tạo ---")
with open("nhanvien.txt", "r") as f:
    print(f.read())
