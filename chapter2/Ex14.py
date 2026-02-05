import math

try:
    n = int(input("Nhập vào một số nguyên dương: "))
    if n <= 1:
        print(f"{n} không phải là số nguyên tố.")
    else:
        is_prime = True # Giả định ban đầu n là số nguyên tố
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False # Tìm thấy ước số khác, không phải số nguyên tố
                break # Thoát vòng lặp ngay lập tức
        if is_prime:
            print(f"{n} là số nguyên tố.")
        else:
            print(f"{n} không phải là số nguyên tố.")

except ValueError:
    print("Lỗi! Vui lòng nhập một số nguyên.")
