# -----------------------------
# Game classes
# -----------------------------
from settings import COLS
from shapes import SHAPES
from utils import shape_to_cells


class Piece:
    def __init__(self, kind):
        self.kind = kind
        self.rot = 0
        self.x = COLS // 2 - 2
        self.y = -1  # start slightly above
        self.states = SHAPES[kind]

    @property
    def grid(self):
        return self.states[self.rot % len(self.states)]

    def cells(self, dx=0, dy=0, rot_delta=0):
        next_rot = (self.rot + rot_delta) % len(self.states)
        grid = self.states[next_rot]
        return shape_to_cells(grid, self.x + dx, self.y + dy)
