try:
    age = int(input("Vui lòng nhập tuổi của bạn: "))
    if 1 <= age <= 120:
        print(f"Tuổi {age} hợp lệ. Cảm ơn bạn!")
    else:
        print(f"Tuổi {age} không hợp lệ! Vui lòng nhập số trong khoảng từ 1 đến 120.")
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
