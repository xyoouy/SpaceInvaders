

class Speed:
    def __init__(self, level):
        self.speed = 45 + level
        self.move_timer = 1 - level/100