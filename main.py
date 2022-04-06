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

# Returns puzzle completely solved if valid
def solver(puzzle):
    print("doing stuff")
    # iterate over each of the rows.
    for row in puzzle:
        # iterate over each of the columns.
        for cell_column in range(len(row)):
            # if we find an unfilled cell, check all the numbers 1-9 and see if there is a single possible choice.
            # if there is a single choice fill it in and continue.
            if row[cell_column] == 0:
                only_possible_number = False;
                for number in range(1, 10):
                    if only_possible_number is True:
                        temp = validate(puzzle, row, cell_column, number)
                        if temp is True:
                            print(row)
                            print(cell_column)
                            break
                    else:
                        only_possible_number = validate(puzzle, row, cell_column, number)


# Takes individual entry value and determines if it is valid entry returns bool
def validate(puzzle, row, index, value):
    column = getcolumn(puzzle, index)
    boxCoordinate = getboxcoordinates(0, index)
    box = getbox(puzzle, boxCoordinate[0], boxCoordinate[1])
    # already have row so, just use it

    for value in range(9):
        if value not in row and value not in column and value not in box:
            return True

    return False


def getboxcoordinates(y, x):
    boxRow = int(y/3)
    boxColumn = int(x/3)
    return boxRow, boxColumn


# Helper function to grab the box from an index and return that box as an array,
# since we can't use the arrays like we do in each of the rows.
def getbox(puzzle, box_row, box_column):
    rowStartPosition = box_row * 3
    columnStartPosition = box_column * 3
    array = []
    for x in range(rowStartPosition, rowStartPosition+3):
        for y in range(columnStartPosition, columnStartPosition+3):
            array.append(puzzle[x][y])
    return array


# Helper function to grab the column from an index and return that box as an array,
# since we can't use the arrays like we do in each of the rows.
def getcolumn(puzzle, index):
    array = []
    for i in range(9):
        array.append(puzzle[i][index])
    return array


main()
