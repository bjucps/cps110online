class Point:

    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, x_offset: float, y_offset: float):
        self.x += x_offset
        self.y += y_offset
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def distance_to(self, other: 'Point'):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** .5


here = Point(3, 5)
there = Point(x=8, y=5)

print("Distance from", here, "to", there,
      "is:", here.distance_to(there))

print(here)
here.x = 42
print(here)
