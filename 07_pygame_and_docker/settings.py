# -----------------------------
# Config
# -----------------------------
CELL_SIZE = 30
COLS, ROWS = 10, 20
PLAY_W, PLAY_H = COLS * CELL_SIZE, ROWS * CELL_SIZE

PANEL_W = 220
MARGIN = 20

WIN_W = PLAY_W + PANEL_W + MARGIN * 3
WIN_H = PLAY_H + MARGIN * 2

FPS = 60
DROP_MS = 800  # soft gravity
FAST_DROP_MS = 50

BG_COLOR = (18, 18, 22)
GRID_COLOR = (35, 35, 40)
TEXT_COLOR = (230, 230, 235)
PANEL_BG = (28, 28, 34)
BTN_BG = (60, 60, 80)
BTN_BG_HOVER = (90, 90, 120)
BTN_TEXT = (245, 245, 255)

# Tetrimino colors
COLORS = {
    'S': (80, 200, 120),
    'Z': (240, 80, 80),
    'I': (50, 180, 230),
    'O': (240, 220, 90),
    'J': (90, 120, 240),
    'L': (240, 160, 60),
    'T': (180, 90, 200),
}
