from enum import Enum


class Direction(Enum):
    LEFT = 0
    RIGHT = 1


class BulletType(Enum):
    Player = 0
    Enemy = 1


class Color(Enum):
    Cyan = (0, 255, 255)
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Green = (0, 255, 0)
    Pink = (255, 0, 255)
    Yellow = (255, 255, 0)
    Red = (255, 0, 0)
    k = (0, 0, 255)

