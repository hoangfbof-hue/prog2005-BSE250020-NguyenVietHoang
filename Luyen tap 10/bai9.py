class ElectronicDevice:
    _total_devices = 0

    def __init__(self, brand, price):
        if not brand:
            raise ValueError("Thương hiệu không được để trống!")

        self._brand = brand
        self.price = price 
        ElectronicDevice._total_devices += 1
    @property
    def brand(self):
        return self._brand
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Giá tiền không thể là số âm!")
        self._price = value
    def power_on(self):
        return f"{self._brand} đang khởi động..."
    @classmethod
    def get_total_count(cls):
        return f"Tổng số thiết bị: {cls._total_devices}"
    @staticmethod
    def is_electronic(item_name):
        electronics = ["phone", "laptop", "tablet", "tv"]
        return item_name.lower() in electronics
    def __str__(self):
        return f"Thiết bị: {self._brand} | Giá: {self._price}$"
    def __eq__(self, other):
        if isinstance(other, ElectronicDevice):
            return self._brand == other._brand and self._price == other._price
        return False


class Smartphone(ElectronicDevice):
    def __init__(self, brand, price, os):
        super().__init__(brand, price)
        self.os = os
    def make_call(self, number):
        return f"Đang gọi đến {number} bằng hệ điều hành {self.os}..."
    def __str__(self):
        return super().__str__() + f" | Hệ điều hành: {self.os}"


try:
    dev1 = ElectronicDevice("Sony", 500)
    phone1 = Smartphone("Apple", 1000, "iOS")
    phone2 = Smartphone("Apple", 1000, "iOS")
    print("--- Thông tin đối tượng ---")
    print(dev1)
    print(phone1)
    print("\n--- Thử nghiệm Getter/Setter ---")
    phone1.price = 1200
    print(f"Giá mới của {phone1.brand}: {phone1.price}$")
    print("\n--- Phương thức đối tượng ---")
    print(dev1.power_on())
    print(phone1.make_call("0912345678"))
    print("\n--- Class & Static Methods ---")
    print(ElectronicDevice.get_total_count())
    print(f"Laptop có phải đồ điện tử? {ElectronicDevice.is_electronic('laptop')}")
    print("\n--- So sánh đối tượng (==) ---")
    print(f"phone1 có bằng phone2 không? {phone1 == phone2}")

except ValueError as e:
    print(f"Lỗi xác thực: {e}")
