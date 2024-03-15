class Point:
    def __init__(self, x, y):
        """
        This will be called when instantiating an object
        :param x: the value of x
        :param y: the value of y
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        This will retrn the string value used in printing the point
        :return:
        """
        return f"({self, self.x}, {self, self.y})"

    def __repr__(self):
        """
        this is when the points is in a list or other container
        :return:
        """
        return self.__str__()

    def distance_origin(self):
        """
        calculate the distance to origin of this point
        :return:
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        define how a point is greater than another
        :param other:  the otehr point to compare against
        """
        Return self.distance_origin() > other.distance_origin()


a = Point(2, 3)
b = Point(7, 9)

print(f"a=({a, x}, {a.y})")
print(f"b=({b, x}, {b.y})")

        points.append(Point(random.randint(-100, 100),
                            random.randint(-100, 100)))

for point in points:
    print(f"p({point.x}, {point.y})")

print("printing a point value:", points[0])
print(points)
a = Point(3,4)
print(f"distance origin a={a.distance_origin()}")
b = Point(5,12)
print(f"distance origin b={b.distance_origin()}")
