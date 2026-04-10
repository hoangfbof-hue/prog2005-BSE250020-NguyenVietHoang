def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
lst = [10, 5, 7, 2, 11, 7]
lst.append(int(input("Nhập phần tử muốn thêm: ")))
k = int(input("Nhập giá trị k cần đếm: "))
print(f"Số lần xuất hiện của {k}: {lst.count(k)}")
tong_nt = sum(x for x in lst if is_prime(x))
print(f"Tổng các số nguyên tố: {tong_nt}")
lst.sort()
print(f"Danh sách sau khi sắp xếp: {lst}")
lst.clear()
print("Danh sách sau khi xóa:", lst)
