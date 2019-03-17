
border_points = []

def get_points(x_start, y_start, x_end, y_end):

    points = []

    if x_start == x_end:
        if y_end - y_start > 0:
            for y in range(1, y_end - y_start + 1):
                points.append(Point(x_start, y_start + y))
        else:
            for y in range(1, y_start - y_end + 1):
                points.append(Point(x_start, y_start - y))

    if y_start == y_end:
        if x_end - x_start > 0:
            for x in range(1, x_end - x_start + 1):
                points.append(Point(x_start + x, y_start))
        else:
            for x in range(1, x_start - x_end + 1):
                points.append(Point(x_start - x, y_start))

    return points

def valid_points(points):
    if len(points)==0:
        return False

    for point in border_points:
        if not (border_points[0].__eq__(point) and point.__eq__(points[-1])):
            if point in points:
                return False

    return True

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return 'Punkt ' + str(self.x) + ' ' + str(self.y)

    def __len__(self):
        return 1

    r = 3
    def draw(self, canvas, tile_size):
        canvas.create_oval(self.x * tile_size - self.r, self.y * tile_size - self.r, self.x * tile_size + self.r, self.y * tile_size + self.r, fill='blue')
        print(self)