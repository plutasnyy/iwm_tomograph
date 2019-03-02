class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    def __repr__(self):
        return self.__str__()
