import pygame
from algorithms.bfs import bfs
from simulation.grid import Grid
pygame.init()
WIDTH = 800
HEIGHT = 800

ROWS = 20
COLS = 20

CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Slime Pathfinder")

grid = Grid(ROWS, COLS)

path = None
explored = []

explored_index = 0
searching = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if grid.start is not None and grid.goal is not None:
                    path, explored = bfs(grid.cells, grid.start, grid.goal)

                    explored_index = 0
                    searching = True

                    print("Path length:", len(path) if path else 0)
                    print("Cells explored:", len(explored))
            elif event.key == pygame.K_r:
                path = None
                explored = []
                explored_index = 0
                searching = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            col = x // CELL_WIDTH
            row = y // CELL_HEIGHT

            keys = pygame.key.get_pressed()

            if 0 <= row < ROWS and 0 <= col < COLS:

                if keys[pygame.K_s]:
                    grid.set_start(row, col)

                    path = None
                    explored = []
                    explored_index = 0
                    searching = False

                elif keys[pygame.K_f]:
                    grid.set_goal(row, col)

                    path = None
                    explored = []
                    explored_index = 0
                    searching = False


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
                grid.add_wall(row, col)
            elif mouse_buttons[2]:
                grid.erase(row, col)
            path = None
            explored = []
            explored_index = 0
            searching = False

    screen.fill("white")


    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_WIDTH
            y = row * CELL_HEIGHT

            if grid.cells[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    "black",
                    (x, y, CELL_WIDTH, CELL_HEIGHT)
            )

            elif grid.cells[row][col] == 2:
                pygame.draw.rect(
                    screen,
                    "green",
                    (x, y, CELL_WIDTH, CELL_HEIGHT)
                )

            elif grid.cells[row][col] == 3:
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

    if searching:
        if explored_index < len(explored):
            explored_index += 3
        else:
            searching = False

    for row, col in explored[:explored_index]:
        if (row,col) != grid.start and (row,col) != grid.goal:

            x = col * CELL_WIDTH
            y = row * CELL_HEIGHT

            pygame.draw.rect(
                screen,
                "lightgreen",
                (x,y, CELL_WIDTH, CELL_HEIGHT)
            )

            pygame.draw.rect(
                screen,
                "gray",
                (x, y, CELL_WIDTH, CELL_HEIGHT),
                1
            )

    if path and not searching:
        for row, col in path:
            if (row, col) != grid.start and (row, col) != grid.goal:
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
    clock.tick(30)
pygame.quit()


