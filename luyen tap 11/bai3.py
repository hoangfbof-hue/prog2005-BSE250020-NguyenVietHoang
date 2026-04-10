input_str = input("Nhập danh sách số (cách nhau bởi dấu cách): ")
nums = [int(x) for x in input_str.split()]

so_chan = [n for n in nums if n % 2 == 0]
tong_chan = sum(so_chan)

print(f"Các số chẵn: {so_chan}")
print(f"Tổng các số chẵn: {tong_chan}")
