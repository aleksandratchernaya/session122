from point import Point

colors = ["red", "blue", "green", "yellow", "purple", "pink", "beige", "bordeaux", "marsala"]

class ColoredPoint(Point):
    def __init(selfself, x, y):

    def __str__(self):
        return f"{self.color}({self.x}, {self,y})"

colored_points = []
for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-100, 100),
                     random.randint(-100, 100),
                    random.choice(colors))
    )
    