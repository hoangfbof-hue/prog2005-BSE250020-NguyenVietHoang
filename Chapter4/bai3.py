data = {
    "name": "Gemini",
    "version": "3.0",
    "language": "Python"
}
key_to_check = input("Nhập tên khóa cần kiểm tra: ")
if key_to_check in data:
    print(f"Khóa '{key_to_check}' CÓ tồn tại. Giá trị là: {data[key_to_check]}")
else:
    print(f"Khóa '{key_to_check}' KHÔNG tồn tại trong dictionary.")
