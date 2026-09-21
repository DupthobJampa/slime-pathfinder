import pygame

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
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0] or mouse_buttons[2]:
            x, y = pygame.mouse.get_pos()
            col = x // CELL_WIDTH
            row = y // CELL_HEIGHT

            if 0 <= row < ROWS and 0 <= col < COLS:
                if mouse_buttons[0]:
                    grid[row][col] = 1
                elif mouse_buttons[2]:
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

            pygame.draw.rect(
                screen,
                "gray",
                (x, y, CELL_WIDTH, CELL_HEIGHT),
                1
            )
    pygame.display.flip()

pygame.quit()