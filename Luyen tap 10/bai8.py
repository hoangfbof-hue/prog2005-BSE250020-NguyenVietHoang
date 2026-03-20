strings = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i + 1}: ")
    strings.append(s)

print(f"\nDanh sách ban đầu: {strings}")
print("-" * 30)
n = len(strings)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if len(strings[j]) < len(strings[j + 1]):

            strings[j], strings[j + 1] = strings[j + 1], strings[j]
            swapped = True
        print(f"Bước {i + 1}.{j + 1}: {strings}")

    if not swapped:
        break
print("-" * 30)
print("Danh sách sau khi sắp xếp giảm dần theo độ dài:")
for s in strings:
    print(f"'{s}' (Độ dài: {len(s)})")
