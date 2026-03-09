def dem_nguyen_am(chuoi):
    nguyen_am = "aeiou"
    dem = 0
    for ky_tu in chuoi.lower():
        if ky_tu in nguyen_am:
            dem += 1
    return dem
chuoi_nhap = input()
print("Số nguyên âm là:", dem_nguyen_am(chuoi_nhap))