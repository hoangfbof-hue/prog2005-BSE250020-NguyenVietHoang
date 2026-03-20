user_input = input("Nhập vào một chuỗi bất kỳ: ")

if not user_input.strip():
    print("Lỗi: Bạn chưa nhập nội dung nào hoặc chỉ nhập khoảng trắng!")
else:
    do_dai = len(user_input)
    print(f"Độ dài của chuỗi bạn vừa nhập là: {do_dai}")
