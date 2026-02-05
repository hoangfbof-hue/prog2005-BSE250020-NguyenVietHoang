
try:
    n = int(input("Bạn muốn in bao nhiêu số trong dãy Fibonacci? n = "))

    if n <= 0:
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    elif n == 1:
        print("Dãy Fibonacci: 0")
    else:
        f0, f1 = 0, 1
        count = 0

        print(f"{n} số đầu tiên trong dãy Fibonacci là:")
        while count < n:
            print(f0, end="  ")
            f_next = f0 + f1
            f0 = f1
            f1 = f_next

            count += 1
        print()

except ValueError:
    print("Lỗi! Vui lòng nhập vào một số nguyên.")
