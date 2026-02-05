num_str = input("Nhập vào một số dương: ")
if num_str.isdigit():
    so_dao_nguoc = num_str[::-1]
    print(f"Số sau khi đảo ngược là: {so_dao_nguoc}")
else:
    print("Vui lòng chỉ nhập các chữ số dương!")
