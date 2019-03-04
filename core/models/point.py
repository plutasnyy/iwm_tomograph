class Point(object):
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y

    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
