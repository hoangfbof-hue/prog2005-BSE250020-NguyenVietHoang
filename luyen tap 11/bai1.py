danh_sach = []
for i in range(5):
    danh_sach.append(input(f"Nhập chuỗi thứ {i+1}: "))

print("\nQuá trình sắp xếp Insertion Sort (Giảm dần theo độ dài):")
for i in range(1, len(danh_sach)):
    key = danh_sach[i]
    j = i - 1
    while j >= 0 and len(danh_sach[j]) < len(key):
        danh_sach[j + 1] = danh_sach[j]
        j -= 1
    danh_sach[j + 1] = key
    print(f"Bước {i}: {danh_sach}")

print(f"\nKết quả cuối cùng: {danh_sach}")
