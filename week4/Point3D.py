class Point3D:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'

    # How can I annotate the type of argument "other"(Point3D instance)?
    def distance(self, other: 'Point3D') -> int:
        dist = ((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)**0.5
        return dist


if __name__ == '__main__':
    my_point = Point3D()
    point_2 = Point3D(0, 3, 4)
    print(my_point.distance(point_2))
