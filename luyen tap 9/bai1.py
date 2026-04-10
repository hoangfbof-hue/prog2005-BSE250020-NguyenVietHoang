weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

bmi = weight / (height ** 2)

print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
