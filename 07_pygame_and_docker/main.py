import sys
import random
import pygame

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

# Shapes as rotation states (4x4 grid strings)
SHAPES = {
    'S': [
        ["....",
         "..00",
         ".00.",
         "...."],
        ["....",
         ".0..",
         ".00.",
         "..0."],
    ],
    'Z': [
        ["....",
         ".00.",
         "..00",
         "...."],
        ["....",
         "..0.",
         ".00.",
         ".0.."],
    ],
    'I': [
        ["..0.",
         "..0.",
         "..0.",
         "..0."],
        ["....",
         "0000",
         "....",
         "...."],
    ],
    'O': [
        [".00.",
         ".00.",
         "....",
         "...."],
    ],
    'J': [
        ["....",
         ".0..",
         ".000",
         "...."],
        ["....",
         "..00",
         "..0.",
         "..0."],
        ["....",
         "....",
         ".000",
         "...0"],
        ["....",
         "..0.",
         "..0.",
         ".00."],
    ],
    'L': [
        ["....",
         "...0",
         ".000",
         "...."],
        ["....",
         "..0.",
         "..0.",
         "..00"],
        ["....",
         "....",
         ".000",
         ".0.."],
        ["....",
         ".00.",
         "..0.",
         "..0."],
    ],
    'T': [
        ["....",
         "..0.",
         ".000",
         "...."],
        ["....",
         "..0.",
         "..00",
         "..0."],
        ["....",
         "....",
         ".000",
         "..0."],
        ["....",
         "..0.",
         ".00.",
         "..0."],
    ],
}

# -----------------------------
# Helpers
# -----------------------------
def shape_to_cells(shape_grid, x, y):
    """Convert 4x4 shape grid to absolute (col,row) cell list at position x,y."""
    cells = []
    for r in range(4):
        for c in range(4):
            if shape_grid[r][c] == '0':
                cells.append((x + c, y + r))
    return cells

def valid(cells, grid):
    """Check if cells are in-bounds and not colliding."""
    for cx, cy in cells:
        if cx < 0 or cx >= COLS or cy < 0 or cy >= ROWS:
            return False
        if grid[cy][cx] is not None:
            return False
    return True

def lock_piece(grid, cells, color_key):
    for cx, cy in cells:
        if 0 <= cy < ROWS and 0 <= cx < COLS:
            grid[cy][cx] = color_key

def clear_lines(grid):
    """Clear full rows and return count."""
    new_grid = [row for row in grid if any(cell is None for cell in row)]
    cleared = ROWS - len(new_grid)
    for _ in range(cleared):
        new_grid.insert(0, [None] * COLS)
    return new_grid, cleared

def score_for_lines(lines):
    # 1->100, 2->400, 3->900, 4->1600
    return 100 * (lines ** 2)

# -----------------------------
# Game classes
# -----------------------------
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

# -----------------------------
# Rendering
# -----------------------------
def draw_grid(surface, grid, play_rect):
    # background
    pygame.draw.rect(surface, BG_COLOR, surface.get_rect())
    # playfield
    pygame.draw.rect(surface, (22, 22, 28), play_rect, border_radius=6)
    # panel
    panel_rect = pygame.Rect(play_rect.right + MARGIN, MARGIN, PANEL_W, PLAY_H)
    pygame.draw.rect(surface, PANEL_BG, panel_rect, border_radius=6)

    # grid lines
    for r in range(ROWS):
        for c in range(COLS):
            cell_rect = pygame.Rect(play_rect.x + c * CELL_SIZE,
                                    play_rect.y + r * CELL_SIZE,
                                    CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, GRID_COLOR, cell_rect, 1)

def draw_cells(surface, play_rect, grid):
    for r in range(ROWS):
        for c in range(COLS):
            color_key = grid[r][c]
            if color_key:
                color = COLORS[color_key]
                rect = pygame.Rect(play_rect.x + c * CELL_SIZE + 1,
                                   play_rect.y + r * CELL_SIZE + 1,
                                   CELL_SIZE - 2, CELL_SIZE - 2)
                pygame.draw.rect(surface, color, rect, border_radius=4)

def draw_piece(surface, play_rect, piece):
    color = COLORS[piece.kind]
    for cx, cy in piece.cells():
        if cy >= 0:
            rect = pygame.Rect(play_rect.x + cx * CELL_SIZE + 1,
                               play_rect.y + cy * CELL_SIZE + 1,
                               CELL_SIZE - 2, CELL_SIZE - 2)
            pygame.draw.rect(surface, color, rect, border_radius=4)

def draw_panel(surface, play_rect, score, font, small_font, paused):
    x = play_rect.right + MARGIN
    y = MARGIN + 16

    def blit_line(text, yoff, f=font, color=TEXT_COLOR):
        label = f.render(text, True, color)
        surface.blit(label, (x + 16, yoff))

    blit_line("Score", y)
    blit_line(f"{score}", y + 40, font)
    if paused:
        blit_line("Paused", y + 90, font, (255, 170, 0))

    y2 = y + 150
    blit_line("Controls", y2)
    for i, line in enumerate([
        "←/→: Move",
        "↓: Soft drop",
        "↑ or W: Rotate",
        "Space: Hard drop",
        "P: Pause",
        "Esc: Menu/Quit",
    ]):
        blit_line(line, y2 + 36 + i * 28, small_font)

# -----------------------------
# Menu
# -----------------------------
def menu(screen, font, small_font, clock):
    btn_w, btn_h = 220, 60
    start_rect = pygame.Rect((WIN_W - btn_w)//2, WIN_H//2 - 90, btn_w, btn_h)
    quit_rect  = pygame.Rect((WIN_W - btn_w)//2, WIN_H//2 + 20, btn_w, btn_h)

    while True:
        screen.fill(BG_COLOR)
        title = font.render("Tetris", True, TEXT_COLOR)
        screen.blit(title, (WIN_W//2 - title.get_width()//2, 140))

        mx, my = pygame.mouse.get_pos()
        for rect, label in [(start_rect, "Start"), (quit_rect, "Quit")]:
            hovering = rect.collidepoint(mx, my)
            pygame.draw.rect(screen, BTN_BG_HOVER if hovering else BTN_BG, rect, border_radius=10)
            text = small_font.render(label, True, BTN_TEXT)
            screen.blit(text, (rect.centerx - text.get_width()//2,
                               rect.centery - text.get_height()//2))

        pygame.display.flip()
        clock.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "quit"
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return "quit"
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if start_rect.collidepoint(e.pos):
                    return "start"
                if quit_rect.collidepoint(e.pos):
                    return "quit"

# -----------------------------
# Game loop
# -----------------------------
def game(screen, font, small_font, clock):
    play_rect = pygame.Rect(MARGIN, MARGIN, PLAY_W, PLAY_H)
    grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
    current = Piece(random.choice(list(SHAPES.keys())))
    next_drop = pygame.time.get_ticks() + DROP_MS
    score = 0
    paused = False

    while True:
        dt = clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "quit", score
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return "menu", score
                if e.key in (pygame.K_p,):
                    paused = not paused
                if paused:
                    continue
                if e.key == pygame.K_LEFT:
                    if valid(current.cells(dx=-1), grid):
                        current.x -= 1
                elif e.key == pygame.K_RIGHT:
                    if valid(current.cells(dx=1), grid):
                        current.x += 1
                elif e.key == pygame.K_DOWN:
                    if valid(current.cells(dy=1), grid):
                        current.y += 1
                        next_drop = pygame.time.get_ticks() + DROP_MS
                elif e.key in (pygame.K_UP, pygame.K_w):
                    if valid(current.cells(rot_delta=1), grid):
                        current.rot = (current.rot + 1) % len(current.states)
                elif e.key == pygame.K_SPACE:
                    # hard drop
                    while valid(current.cells(dy=1), grid):
                        current.y += 1
                    # lock immediately
                    lock_piece(grid, current.cells(), current.kind)
                    grid, cleared = clear_lines(grid)
                    if cleared:
                        score += score_for_lines(cleared)
                    current = Piece(random.choice(list(SHAPES.keys())))
                    # if spawn collides -> game over to menu
                    if not valid(current.cells(), grid):
                        return "menu", score

        # gravity
        if not paused and pygame.time.get_ticks() >= next_drop:
            speed = FAST_DROP_MS if pygame.key.get_pressed()[pygame.K_DOWN] else DROP_MS
            if valid(current.cells(dy=1), grid):
                current.y += 1
            else:
                # lock, clear, spawn new
                lock_piece(grid, current.cells(), current.kind)
                grid, cleared = clear_lines(grid)
                if cleared:
                    score += score_for_lines(cleared)
                current = Piece(random.choice(list(SHAPES.keys())))
                if not valid(current.cells(), grid):
                    return "menu", score
            next_drop = pygame.time.get_ticks() + speed

        # draw
        draw_grid(screen, grid, play_rect)
        draw_cells(screen, play_rect, grid)
        draw_piece(screen, play_rect, current)
        draw_panel(screen, play_rect, score, font, pygame.font.SysFont(None, 24), paused)

        pygame.display.flip()

def main():
    pygame.init()
    pygame.display.set_caption("Tetris")
    screen = pygame.display.set_mode((WIN_W, WIN_H))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 36)

    while True:
        choice = menu(screen, font, small_font, clock)
        if choice == "quit":
            break
        if choice == "start":
            state, _score = game(screen, font, small_font, clock)
            if state == "quit":
                break
            # if state == "menu": loop back to menu and keep running

    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
