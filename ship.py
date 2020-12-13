from math import cos, sin, radians


class UnitVector:
    def __init__(self):
        self.origin = (0, 0)
        self.theta = 0

    def rotate(self, angle):
        self.theta += angle
        self.theta %= 360

        if self.theta > 180:
            self.theta -= 360

    def translate(self, *args):
        if len(args) == 1:
            units = args[0]
            curr_x, curr_y = self.origin
            self.origin = (
                curr_x + float(units) * cos(radians(self.theta)),
                curr_y + float(units) * sin(radians(self.theta)),
            )
        elif len(args) == 2:
            [translate_x, translate_y] = args
            curr_x, curr_y = self.origin
            self.origin = (curr_x + translate_x, curr_y + translate_y)

    def __repr__(self):
        return f"Origin: {self.origin} Angle: {self.theta}"


class Ship(UnitVector):
    def move(self, direction, units):
        dispatch_table = {
            "N": self.move_north,
            "E": self.move_east,
            "S": self.move_south,
            "W": self.move_west,
            "L": self.rotate_left,
            "R": self.rotate_right,
            "F": self.move_forward,
        }

        return dispatch_table[direction](units)

    def move_north(self, units):
        self.translate(0, units)

    def move_east(self, units):
        self.translate(units, 0)

    def move_south(self, units):
        self.translate(0, -units)

    def move_west(self, units):
        self.translate(-units, 0)

    def rotate_left(self, units):
        self.rotate(units)

    def rotate_right(self, units):
        self.rotate(-units)

    def move_forward(self, units):
        self.translate(units)
