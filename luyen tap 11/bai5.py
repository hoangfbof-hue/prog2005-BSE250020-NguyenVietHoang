my_dict = {"name": "Alice", "age": 25, "job": "Dev"}
key_to_check = input("Nhập key cần kiểm tra: ")

if key_to_check in my_dict:
    print(f"Key '{key_to_check}' có tồn tại. Giá trị: {my_dict[key_to_check]}")
else:
    print(f"Key '{key_to_check}' không tồn tại.")
