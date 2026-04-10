target = input("\nNhập chuỗi cần tìm: ")
low = 0
high = len(danh_sach) - 1
vi_tri = -1

while low <= high:
    mid = (low + high) // 2
    if danh_sach[mid] == target:
        vi_tri = mid
        break
    elif len(danh_sach[mid]) < len(target):
        high = mid - 1
    else:
        low = mid + 1

if vi_tri != -1:
    print(f"Tìm thấy chuỗi '{target}' tại vị trí index: {vi_tri}")
else:
    print("Không tìm thấy chuỗi trong danh sách.")
