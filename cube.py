from collections import defaultdict
from copy import deepcopy


class Cube:
    def __init__(self, initial_state, dimensions):
        self.dimensions = dimensions
        self.cube = self.read_initial_state(initial_state)

    def read_initial_state(self, initial_state):
        cube = defaultdict(lambda: ".")
        y = 0

        for row in initial_state.split("\n"):
            x = 0

            for col in list(row):
                coord = tuple([*([0] * (self.dimensions - 2)), y, x])
                cube[coord] = col
                x += 1

            y += 1

        return cube

    def simulate_cycle(self):
        new_cube = deepcopy(self.cube)

        ranges = tuple(
            [range(start - 1, end + 2) for start, end in self.get_coordinate_ranges()]
        )

        def _evaluate_coord(coord):
            coord = tuple(coord)
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

        self.recursive_for(ranges, _evaluate_coord)

        self.cube = new_cube

    def recursive_for(cls, ranges, function, index=0, iters=[]):
        number_of_loops = len(ranges)

        if len(iters) == 0:
            iters = [0] * number_of_loops

        if index == number_of_loops - 1:
            for iters[index] in ranges[index]:
                function(iters)
        else:
            for iters[index] in ranges[index]:
                cls.recursive_for(ranges, function, index + 1, iters)

    def get_coordinate_ranges(self):
        axes = list(zip(*self.cube.keys()))

        return tuple([(min(coords), max(coords)) for coords in axes])

    def get_all_neighboring_coordinates(cls, coord):
        coords = []

        ranges = [range(axis - 1, axis + 2) for axis in coord]

        def _get_neighboring_coordinate(inner_coord):
            if all([inner_coord[i] == coord[i] for i in range(len(inner_coord))]):
                return

            coords.append(tuple(inner_coord))

        cls.recursive_for(ranges, _get_neighboring_coordinate)

        return coords

    def count_active(self):
        count = 0
        for coord in self.cube:
            count += int(self.cube[coord] == "#")

        return count
