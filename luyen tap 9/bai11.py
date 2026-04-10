class SinhVien:
    count = 0

    def __init__(self, ten):
        self.ten = ten
        SinhVien.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

s1 = SinhVien("A")
s2 = SinhVien("B")
s3 = SinhVien("C")

print(f"Tổng số sinh viên đã tạo: {SinhVien.get_count()}")
