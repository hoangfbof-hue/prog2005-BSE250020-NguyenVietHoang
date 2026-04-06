def count_vowels(s):
    vowels = "aeiou"
    count = 0
    s_lower = s.lower()
    for char in s_lower:
        if char in vowels:
            count += 1
            
    return count
chuoi_nhap = input("Nhập vào một chuỗi bất kỳ: ")
ket_qua = count_vowels(chuoi_nhap)

print(f"Số lượng nguyên âm trong chuỗi là: {ket_qua}")
