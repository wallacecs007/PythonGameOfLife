#Game of Life Command Line Program
#
#Developed By: Charles Wallace
#Version: 1.0 (Doubt there can be more than one version unless I want to make it super complex
#
#The game of life works off of the following rules:
#A cell that is labeled '#' is alive, and a cell that is labeled ' ' is dead.
#If a dead cell has exactly 3 neighboring cells than it will come to life,
#if an already alive cell has 2 or 3 neighbors it will stay alive.
#And finally if a cell has 0, 1, or more than 3 neighbors it will die or stay dead.
#
# [ [' ', '#', ' ', '#', ' '],
#   [' ', '#', ' ', '#', ' '],
#   [' ', '#', ' ', '#', ' '],
#   [' ', '#', ' ', '#', ' '],
#   [' ', '#', ' ', '#', ' '] ]

import time, random, copy

#Declaring the size of the "board"
Height = 10
Width = 10

#Declaring a 'grid' container to hold rows
nextGrid = []

for x in range(Width):
    #Declaring a row and poppulating
    row = []
    for y in range(Height):
        if random.randint(0, 1) == 0:
            row.append('#')
        else:
            row.append(' ')
    nextGrid.append(row)

while True:

    print('\n\n\n\n\n')

    currentGrid = copy.deepcopy(nextGrid)

    gridOut = ''

    for x in range(Width):
        for y in range(Height):
            gridOut += currentGrid[x][y]
        gridOut += '\n'
    print(gridOut)

    for x in range(Width):
        for y in range(Height):
            #Using remainders to validate that no coordniates are outside of the grid.
            leftCord = (y - 1) % Height
            rightCord = (y + 1) % Height
            topCord = (x - 1) % Width
            bottomCord = (x + 1) % Width

            neighbors = 0
            if currentGrid[topCord][leftCord] == '#':
                neighbors += 1
            if currentGrid[topCord][y] == '#':
                neighbors += 1
            if currentGrid[topCord][rightCord] == '#':
                neighbors += 1
            if currentGrid[x][leftCord] == '#':
                neighbors += 1
            if currentGrid[x][rightCord] == '#':
                neighbors += 1
            if currentGrid[bottomCord][leftCord] == '#':
                neighbors += 1
            if currentGrid[bottomCord][y] == '#':
                neighbors += 1
            if currentGrid[bottomCord][rightCord] == '#':
                neighbors += 1

            if currentGrid[x][y] == '#' and (neighbors == 2 or neighbors == 3):
                nextGrid[x][y] = '#'
            elif currentGrid[x][y] == ' ' and neighbors == 3:
                nextGrid[x][y] = '#'
            else:
                nextGrid[x][y] = ' '

    time.sleep(1)