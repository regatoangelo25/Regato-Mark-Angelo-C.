class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Usage:
rect = Rectangle(5, 10)
print(f"Rectangle area: {rect.area()}")