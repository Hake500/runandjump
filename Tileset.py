# Verwaltet die Tileset Grafik und eine Liste mit Tile-Typen.
import Helper
from TileType import TileType


class Tileset(object):
    # Im Konstruktor laden wir die Grafik
    # und erstellen ein leeres Dictionary für die Tile-Typen.
    def __init__(self, image, colorkey, tile_width, tile_height):
        self.image = Helper.loadImage(image, colorkey)
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_types = dict()

    def add_tile(self, name, start_x, start_y):
        self.tile_types[name] = TileType(name, start_x, start_y, self.tile_width, self.tile_height)

    def get_tile(self, name):
        try:
            return self.tile_types[name]
        except KeyError:
            return None