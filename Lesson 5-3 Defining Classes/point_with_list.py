def makePoint(x: int, y: int):
    return [x, y]

def move(point: list, offsetX: int, offsetY: int):
    point[0] += offsetX
    point[1] += offsetY

def distance(point1: list, point2: list):
    return ((point1[0] - point2[0]) ** 2 
              + (point1[1] - point2[1]) ** 2) ** .5

def to_str(point: list):
    return "({0},{1})".format(point[0], point[1])

here = makePoint(3, 2)
there = makePoint(8, 5)

move(here, 10, 5)

print(f"here = ({here[0]},{here[1]})")
print(f"there = {to_str(there)}")

print("Distance from", to_str(here), "to", to_str(there),
      "is:", distance(here, there))

print("Setting there's Y to 10.")
there[1] = 10
print("there =", to_str(there))
