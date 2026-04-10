class Flower:
    def __init__(self, color=""):
        self.__color = color 

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color
hoa_hong = Flower()
hoa_hong.set_color("Red")
print(f"Màu của hoa là: {hoa_hong.get_color()}")
