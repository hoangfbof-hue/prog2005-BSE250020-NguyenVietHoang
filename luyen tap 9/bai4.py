s = input("Nhập một chuỗi: ")

hoa = thuong = so = dac_biet = trang = nguyen_am = phu_am = 0
vowels = "aeiouAEIOU"

for char in s:
    if char.isupper(): hoa += 1
    if char.islower(): thuong += 1
    if char.isdigit(): so += 1
    if char.isspace(): trang += 1
    
    if char.isalpha():
        if char.lower() in "aeiou":
            nguyen_am += 1
        else:
            phu_am += 1
    elif not char.isalnum() and not char.isspace():
        dac_biet += 1

print(f"- In hoa: {hoa}\n- In thường: {thuong}\n- Chữ số: {so}")
print(f"- Khoảng trắng: {trang}\n- Ký tự đặc biệt: {dac_biet}")
print(f"- Nguyên âm: {nguyen_am}\n- Phụ âm: {phu_am}")
