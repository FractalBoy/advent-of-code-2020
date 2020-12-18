from collections import defaultdict
from copy import deepcopy


class Cube:
    def __init__(self, initial_state):
        self.cube = self.read_initial_state(initial_state)

    def read_initial_state(self, initial_state):
        cube = defaultdict(lambda: ".")
        y = 0

        for row in initial_state.split("\n"):
            x = 0
            for col in list(row):

                cube[0, y, x] = col
                x += 1

            y += 1

        return cube

    def simulate_cycle(self):
        new_cube = deepcopy(self.cube)

        min_z, max_z, min_y, max_y, min_x, max_x = self.get_coordinate_ranges()

        for z in range(min_z - 1, max_z + 2):
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):
                    coord = z, y, x

                    neighbors = self.get_all_neighboring_coordinates(coord)

                    active_neighbors = 0

                    for neighbor in neighbors:
                        if self.cube[neighbor] == "#":
                            active_neighbors += 1

                    if self.cube[coord] == "#":
                        if active_neighbors == 2 or active_neighbors == 3:
                            new_cube[coord] = "#"
                        else:
                            new_cube[coord] = "."
                    elif self.cube[coord] == ".":
                        if active_neighbors == 3:
                            new_cube[coord] = "#"
                        else:
                            new_cube[coord] = "."

        self.cube = new_cube

    def get_coordinate_ranges(self):
        [zs, ys, xs] = list(zip(*self.cube.keys()))

        min_z = min(zs)
        max_z = max(zs)

        min_y = min(ys)
        max_y = max(ys)

        min_x = min(xs)
        max_x = max(xs)

        return min_z, max_z, min_y, max_y, min_x, max_x

    def get_all_neighboring_coordinates(cls, coord):
        coords = []

        z, y, x = coord

        for a in range(z - 1, z + 2):
            for b in range(y - 1, y + 2):
                for c in range(x - 1, x + 2):
                    if a == z and b == y and c == x:
                        continue

                    coords.append((a, b, c))

        return coords

    def count_active(self):
        count = 0
        for coord in self.cube:
            count += int(self.cube[coord] == "#")

        return count

    def __str__(self):
        min_z, max_z, min_y, max_y, min_x, max_x = self.get_coordinate_ranges()

        string = ""

        for z in range(min_z, max_z + 1):
            string += f"z={z}\n\n"

            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    string += self.cube[z, y, x]

                string += "\n"

            string += "\n"

        return string
