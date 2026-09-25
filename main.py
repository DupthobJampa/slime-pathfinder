import pygame
from algorithms.bfs import bfs
pygame.init()
WIDTH = 800
HEIGHT = 800

ROWS = 20
COLS = 20

CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slime Pathfinder")

grid = []
for row in range(ROWS):
    grid.append([0] * COLS)

start = None
goal = None
path = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start is not None and goal is not None:
                    path = bfs(grid, start, goal)
            elif event.key == pygame.K_r:
                path = None

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // CELL_WIDTH
            row = y // CELL_HEIGHT
            keys = pygame.key.get_pressed()

            if keys[pygame.K_s] and grid[row][col] != 3:
                if start is not None:
                    old_row, old_col = start
                    grid[old_row][old_col] = 0
                start = (row, col)
                grid[row][col] = 2

            elif keys[pygame.K_f] and grid[row][col] != 2:
                if goal is not None:
                    old_row, old_col = goal
                    grid[old_row][old_col] = 0
                goal = (row, col)
                grid[row][col] = 3


    mouse_buttons = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    if (mouse_buttons[0] or mouse_buttons[2]) and not (
        keys[pygame.K_s] or keys[pygame.K_f]
        ):
            x, y = pygame.mouse.get_pos()
            col = x // CELL_WIDTH
            row = y // CELL_HEIGHT

            if 0 <= row < ROWS and 0 <= col < COLS:
                if mouse_buttons[0]:
                    if grid[row][col] not in (2, 3):
                        grid[row][col] = 1

                elif mouse_buttons[2]:
                    if grid[row][col] == 2:
                        start = None

                    elif grid[row][col] == 3:
                        goal = None
                    grid[row][col] = 0

    screen.fill("white")

    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_WIDTH
            y = row * CELL_HEIGHT

            if grid[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    "black",
                    (x, y, CELL_WIDTH, CELL_HEIGHT)
            )

            elif grid[row][col] == 2:
                pygame.draw.rect(
                    screen,
                    "green",
                    (x, y, CELL_WIDTH, CELL_HEIGHT)
                )

            elif grid[row][col] == 3:
                pygame.draw.rect(
                    screen,
                    "red",
                    (x, y, CELL_WIDTH, CELL_HEIGHT)
                )

            pygame.draw.rect(
                screen,
                "gray",
                (x, y, CELL_WIDTH, CELL_HEIGHT),
                1
            )

    if path:
        for row, col in path:
            if (row, col) != start and (row, col) != goal:
                x = col * CELL_WIDTH
                y = row * CELL_HEIGHT

                pygame.draw.rect(
                    screen,
                    "yellow",
                    (x, y, CELL_WIDTH, CELL_HEIGHT)
                )

                pygame.draw.rect(
                    screen,
                    "gray",
                    (x, y, CELL_WIDTH, CELL_HEIGHT),
                    1
                )

    pygame.display.flip()

pygame.quit()


