class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

    def __eq__(self, other):
        return self.diem == other.diem

sv1 = SinhVien("Hoang", 8.5)
sv2 = SinhVien("Hung", 8.5)

if sv1 == sv2:
    print("Hai sinh viên có điểm bằng nhau.")
else:
    print("Điểm hai sinh viên khác nhau.")
