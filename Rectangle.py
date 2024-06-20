class Rectangle:

    def __init__(self, height, widht):
        self.height = height
        self.width = widht

    def calculate_area(self):
        return self.width * self.height

rectangle = Rectangle(2,4)

print(f'the area of the rectangle is: {rectangle.calculate_area()}')