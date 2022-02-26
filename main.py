# This is a fun Sudoku generator and solver created by Peter and Harvey.
# May god have mercy on our souls (T.T)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import generator


def main():
    # Use a breakpoint in the code line below to debug your script.
    puzzle = generator.generate()
    print("Welcome to our Sudoku solver! Here is the current puzzle :)")
    # for row in puzzle:
    #     print(row)
    solver(puzzle)


def solver(puzzle):
    print("doing stuff")
    for row in puzzle: # this isnt right. We want the position of the row, since we need it in validate.
        for index in range(len(row)):
            if row[index] == 0:
                validate(puzzle, row, index, row[index], 1) # Value needs to be iterated, not hard codes. So should be 1-9

            print('This is index {} with value {}'.format(index, row[index]))


def validate(puzzle, row, index, value):
    column = getcolumn(puzzle, index)
    boxCoordinate = getboxcoordinates(0, index)
    box = getbox(puzzle, boxCoordinate[0], boxCoordinate[1])

    for value in range(9):
        if value not in row and value not in column and value not in box:
            return True


def getboxcoordinates(y, x):
    boxRow = int(y/3)
    boxColumn = int(x/3)
    return boxRow, boxColumn


def getbox(puzzle, boxRow, boxColumn):
    rowStartPosition = boxRow * 3
    columnStartPosition = boxColumn * 3
    array = []
    for x in range(rowStartPosition, rowStartPosition+3):
        for y in range(columnStartPosition, columnStartPosition+3):
            array.append(puzzle[x][y])
    return array


def getcolumn(puzzle, index):
    array = []
    for i in range(9):
        array.append(puzzle[i][index])
    return array
