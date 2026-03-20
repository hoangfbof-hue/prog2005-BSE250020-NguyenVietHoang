string = input("Nhập vào chuỗi cần đảo ngược: ")

reversed_string = ""
for char in string:
    reversed_string = char + reversed_string

print(f"Chuỗi sau khi đảo ngược là: {reversed_string}")
