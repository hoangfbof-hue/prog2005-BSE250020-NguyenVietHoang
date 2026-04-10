data = {}
n = int(input("Bạn muốn nhập bao nhiêu người? "))

for _ in range(n):
    ten = input("Nhập tên: ")
    tuoi = int(input("Nhập tuổi: "))
    data[ten] = tuoi

avg_age = sum(data.values()) / len(data) if data else 0
print(f"Dữ liệu: {data}")
print(f"Tuổi trung bình: {avg_age:.2f}")
