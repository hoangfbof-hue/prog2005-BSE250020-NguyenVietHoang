def is_even(n):
    """
    Trả về True nếu n là số chẵn, False nếu là số lẻ.
    """
    return n % 2 == 0
so_can_kiem_tra = 10
ket_qua = is_even(so_can_kiem_tra)

print(f"Số {so_can_kiem_tra} có phải là số chẵn không? {ket_qua}")
print(f"Số 7 có phải là số chẵn không? {is_even(7)}")
