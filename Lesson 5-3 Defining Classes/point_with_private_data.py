class Point:
    def __init__(self, initX: float, initY: float):
        self.__x = initX
        self.__y = initY
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, newX):
        self.__x = newX
    
    def setY(self, newY):
        self.__y = newY
    
    def __str__(self):
        return "({0},{1})".format(self.__x, self.__y)
    
    def distance_to(self, other):
        return ((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2) ** .5


def update(p: Point):
    #p.__x = p.__x + 10
    p.setX(p.getX() + 10)


here = Point(3, 5)
there = Point(8, 5)

update(there)


print("Distance from", here, "to", there,
      "is:", here.distance_to(there))

print(here)
here.setX(42)
print(here)
