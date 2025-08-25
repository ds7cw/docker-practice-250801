import sys
import random
import pygame

from board import draw_cells, draw_grid, draw_panel, draw_piece
from piece import Piece
from settings import (BG_COLOR, BTN_BG, BTN_BG_HOVER, BTN_TEXT, COLS, DROP_MS, 
    FAST_DROP_MS, FPS, MARGIN, PLAY_H, PLAY_W, ROWS, TEXT_COLOR, WIN_H, WIN_W) 
from shapes import SHAPES
from utils import valid, score_for_lines, clear_lines, lock_piece

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
