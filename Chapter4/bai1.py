def thong_ke_tuple(tup):
    """
    Hàm nhận vào một tuple và trả về tổng, GTLN, GTNN.
    """
    if not tup:
        return 0, None, None

    tong = sum(tup)
    lon_nhat = max(tup)
    nho_nhat = min(tup)

    return tong, lon_nhat, nho_nhat

numbers = (5, 12, 8, -2, 20, 7)
tong, max_val, min_val = thong_ke_tuple(numbers)
print(f"Tuple đầu vào: {numbers}")
print("-" * 25)
print(f"Tổng các phần tử: {tong}")
print(f"Giá trị lớn nhất:  {max_val}")
print(f"Giá trị nhỏ nhất:  {min_val}")
