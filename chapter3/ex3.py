mau = ["Red", "Blue", "Green", "Yellow", "Black"]
try:
    mau.remove("Green")
except ValueError:
    print("Không tìm thấy Green")
print("Danh sách sau khi xử lý:", mau)