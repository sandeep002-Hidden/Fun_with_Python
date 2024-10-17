import pygame
from random import choice

def generate_maze(WIDTH=1200, HEIGHT=600, Tile=30):
    res = WIDTH, HEIGHT
    cols, rows = WIDTH // Tile, HEIGHT // Tile
    pygame.init()
    sc = pygame.display.set_mode(res)
    clock = pygame.time.Clock()
    totalCells = cols * rows
    maze_finished = False

    class Cell:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.walls = {"top": True, "right": True, "bottom": True, "left": True}
            self.visited = False

        def currentCell(self):
            x, y = self.x * Tile, self.y * Tile
            pygame.draw.rect(sc, pygame.Color("black"), (x + 2, y + 2, Tile - 2, Tile - 2))

        def draw(self):
            x, y = self.x * Tile, self.y * Tile
            if self.visited:
                pygame.draw.rect(sc, pygame.Color("black"), (x, y, Tile, Tile))
            if self.walls['top']:
                pygame.draw.line(sc, pygame.Color("blue"), (x, y), (x + Tile, y), 2)
            if self.walls['right']:
                pygame.draw.line(sc, pygame.Color("blue"), (x + Tile, y), (x + Tile, y + Tile), 2)
            if self.walls['left']:
                pygame.draw.line(sc, pygame.Color("blue"), (x, y + Tile), (x, y), 2)
            if self.walls['bottom']:
                pygame.draw.line(sc, pygame.Color("blue"), (x + Tile, y + Tile), (x, y + Tile), 2)

        def checkCell(self, x, y):
            findIndex = lambda x, y: x + y * cols
            if x < 0 or x >= cols or y < 0 or y >= rows:
                return False
            return gridCells[findIndex(x, y)]

        def checkNeighbours(self):
            neighbors = []
            top = self.checkCell(self.x, self.y - 1)
            right = self.checkCell(self.x + 1, self.y)
            bottom = self.checkCell(self.x, self.y + 1)
            left = self.checkCell(self.x - 1, self.y)
            if top and not top.visited:
                neighbors.append(top)
            if right and not right.visited:
                neighbors.append(right)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if left and not left.visited:
                neighbors.append(left)
            return choice(neighbors) if neighbors else False

    def remove_walls(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False

    gridCells = [Cell(col, row) for row in range(rows) for col in range(cols)]
    currentCell = gridCells[0]
    stack = []
    visitedCount = 0

    while True:
        sc.fill(pygame.Color("black"))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
        
        # Draw the maze grid
        [cell.draw() for cell in gridCells]
        
        if not maze_finished:
            currentCell.visited = True
            currentCell.currentCell()

            nextCell = currentCell.checkNeighbours()
            if nextCell:
                nextCell.visited = True
                visitedCount += 1
                stack.append(currentCell)
                remove_walls(currentCell, nextCell)
                currentCell = nextCell
            elif stack:
                currentCell = stack.pop()

            if totalCells - 1 == visitedCount:
                maze_finished = True 
                print("Maze construction finished")

        pygame.display.flip()
        clock.tick(20)
