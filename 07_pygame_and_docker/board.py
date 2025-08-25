# -----------------------------
# Rendering
# -----------------------------
import pygame

from settings import (BG_COLOR, CELL_SIZE, COLORS, COLS, GRID_COLOR, MARGIN,
    PANEL_BG, PANEL_W, PLAY_H, ROWS, TEXT_COLOR)


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
