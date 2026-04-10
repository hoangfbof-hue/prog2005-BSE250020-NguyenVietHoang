class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split("-")
        return cls(name, int(age))

p = Person.from_string("Nam-20")
print(f"Tên: {p.name}, Tuổi: {p.age}")
