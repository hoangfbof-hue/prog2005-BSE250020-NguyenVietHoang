try:
    num1 = int(input("Nhập số bị chia (số nguyên): "))
    num2 = int(input("Nhập số chia (số nguyên): "))
    result = num1 / num2
    print(f"Kết quả của {num1} / {num2} là: {result}")

except ZeroDivisionError:
    print("Lỗi: Không thể thực hiện phép chia cho số 0!")

except ValueError:
    print("Lỗi: Dữ liệu nhập vào không hợp lệ. Vui lòng chỉ nhập số nguyên.")

except Exception as e:
    print(f"Đã xảy ra lỗi không xác định: {e}")
