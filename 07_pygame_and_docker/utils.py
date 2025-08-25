# -----------------------------
# Helpers
# -----------------------------
from settings import ROWS, COLS


def shape_to_cells(shape_grid, x, y):
    """Convert 4x4 shape grid to absolute (col,row) cell list at position x,y."""
    cells = []
    for r in range(4):
        for c in range(4):
            if shape_grid[r][c] == '0':
                cells.append((x + c, y + r))
    return cells

def valid(cells, grid):
    """Check if cells are in-bounds and not colliding with locked pieces."""
    for cx, cy in cells:
        if cy < 0:
            continue
        if cx < 0 or cx >= COLS or cy >= ROWS:
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
