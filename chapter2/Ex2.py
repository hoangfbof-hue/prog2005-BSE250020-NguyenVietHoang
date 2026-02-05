import math
try:
    n = int(input("Nhập vào một số nguyên dương: "))
    if n <= 1:
        print(f"{n} không phải là số nguyên tố.")
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{n} là số nguyên tố!")
        else:
            print(f"{n} không phải là số nguyên tố.")

except ValueError:
    print("Vui lòng chỉ nhập số nguyên!")
