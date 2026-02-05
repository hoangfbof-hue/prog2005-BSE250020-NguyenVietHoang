try:
    s = input("Nhập vào một số nguyên dương có 5 chữ số: ")
    if s.isdigit() and len(s) == 5:
        max_digit = s[0] 
        
        for chu_so in s:
            if chu_so > max_digit:
                max_digit = chu_so
        
        print(f"Chữ số lớn nhất trong số {s} là: {max_digit}")

    else:
        print("Lỗi: Vui lòng nhập đúng một số nguyên dương có 5 chữ số!")

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
