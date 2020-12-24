#!/usr/bin/env python

import re
from collections import defaultdict
from itertools import product
from functools import reduce
from operator import mul

from aoc_input import read_full_text
from tile import Tile


def main():
    text = read_full_text(2020, 20)
    tiles = {
        int(id_): Tile(tile)
        for id_, tile in re.findall(r"Tile (\d+):\n([\.#\n]+)", text)
    }

    matches = defaultdict(lambda: 0)

    for tile_a, tile_b in product(tiles, tiles):
        if tile_a == tile_b:
            continue

        matches[tile_a] += len(tiles[tile_a].match_tile(tiles[tile_b]))

    print(reduce(mul, (id_ for id_, matches in matches.items() if matches == 2)))


if __name__ == "__main__":
    main()
