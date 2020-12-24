from collections import defaultdict
from math import cos, sin, radians


class Tile:
    def __init__(self, tile):
        if isinstance(tile, str):
            self.read_in_tile(tile)

        else:
            self.tile = tile

    def read_in_tile(self, tile):
        self.tile = defaultdict(lambda: " ")

        y = 0

        for row in tile.splitlines():
            x = 0

            for col in row:
                self.tile[x, y] = col
                x += 1

            y += 1

    def edges(self):
        edges = []

        width, height = self.dimensions()

        edge = []

        # Top
        for x in range(width):
            edge.append(self.tile[x, 0])

        edges.append(edge)
        edge = []

        # Left
        for y in range(height):
            edge.append(self.tile[0, y])

        edges.append(edge)
        edge = []

        # Bottom
        for x in range(width):
            edge.append(self.tile[x, height - 1])

        edges.append(edge)
        edge = []

        # Right
        for y in range(width):
            edge.append(self.tile[width - 1, y])

        edges.append(edge)

        return tuple(edges)

    def match_tile(self, other):
        if self == other:
            return []

        my_edges = self.edges()
        their_edges = other.edges()

        matched = []

        for my_edge in my_edges:
            for their_edge in their_edges:
                if my_edge == their_edge or my_edge == list(reversed(their_edge)):
                    matched.append(my_edge)

        return matched

    def extend_corner(self, tiles):
        my_top, my_left, my_bottom, my_right = self.edges()
        edge_matches = {}

        for tile in tiles:
            edges = self.match_tile(tile)

            if len(edges):
                edge_matches[tile] = edges[0]

        if len(edge_matches) != 2:
            raise Exception("this tile must be a corner in order to extend it")

        tile_matches = list(edge_matches.keys())

        for tile in tiles:
            matches_0 = tile.match_tile(tile_matches[0])
            matches_1 = tile.match_tile(tile_matches[1])

            if len(matches_0) and len(matches_1):
                third_tile = tile
                third_edge = matches_0

        new_tile = {(0, 0): self}

        for tile in edge_matches:
            if edge_matches[tile] == my_top:
                new_tile[0, 1] = tile
            elif edge_matches[tile] == my_left:
                new_tile[-1, 0] = tile
            elif edge_matches[tile] == my_bottom:
                new_tile[0, -1] = tile
            elif edge_matches[tile] == my_right:
                new_tile[1, 0] = tile

        third_coord = tuple(map(sum, zip(*new_tile.keys())))
        new_tile[third_coord] = third_tile

        row_a = [tile for coord, tile in new_tile.items() if coord[1] == 0]
        row_b = [tile for coord, tile in new_tile.items() if coord[1] == 1]

        row_a = row_a[0].patch_horizontal(row_a[1])
        row_b = row_b[0].patch_horizontal(row_b[1])
        print(row_a.patch_vertical(row_b))

    def dimensions(self):
        [xs, ys] = zip(*self.tile.keys())
        return (max(xs) - min(xs) + 1, max(ys) - min(ys) + 1)

    def patch_horizontal(self, other):
        width, height = self.dimensions()
        new_tile = defaultdict(lambda: " ")

        for y in range(height - 1):
            for x in range(width - 1):
                new_tile[x, y] = self.tile[x, y]

            for x in range(1, width):
                new_tile[x + width, y] = other.tile[x, y]

        return Tile(new_tile)

    def patch_vertical(self, other):
        width, height = self.dimensions()
        new_tile = defaultdict(lambda: " ")

        for y in range(height - 1):
            for x in range(width):
                new_tile[x, y] = self.tile[x, y]

        for y in range(1, height):
            for x in range(width):
                new_tile[x, y + height] = other.tile[x, y]

        return Tile(new_tile)

    def __str__(self):
        width, height = self.dimensions()

        string = ""

        for y in range(height):
            for x in range(width):
                string += self.tile[x, y]

            string += "\n"

        return string
