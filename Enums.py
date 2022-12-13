from enum import Enum


class Direction(Enum):
    LEFT = 0
    RIGHT = 1


class BulletType(Enum):
    Player = 0
    Enemy = 1


class Color(Enum):
    Blue = (0, 255, 255)
    White = (255, 255, 255)
    Black = (0, 0, 0)
