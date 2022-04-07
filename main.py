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
    puzzle = solver(puzzle)
    print("This is your puzzle after running solver :) ")
    for row in puzzle:
        print(row)
    puzzle = solver(puzzle)
    print("This is your puzzle after running solver :) ")
    for row in puzzle:
        print(row)
    puzzle = solver(puzzle)
    print("This is your puzzle after running solver :) ")
    for row in puzzle:
        print(row)
    puzzle = solver(puzzle)
    print("This is your puzzle after running solver :) ")
    for row in puzzle:
        print(row)
    puzzle = solver(puzzle)
    print("This is your puzzle after running solver :) ")
    for row in puzzle:
        print(row)
    puzzle = solver(puzzle)
    print("This is your puzzle after running solver :) ")
    for row in puzzle:
        print(row)

# Returns puzzle completely solved if valid
def solver(puzzle):
    print("doing stuff")
    # iterate over each of the rows.
    for row_number in range(len(puzzle)):
        row = puzzle[row_number]
        # print('Row {}'.format(row))
        # iterate over each of the columns.
        for column_number in range(len(row)):
            # if we find an unfilled cell, check all the numbers 1-9 and see if there is a single possible choice.
            # if there is a single choice fill it in and continue.
            if row[column_number] == 0:
                # Begin with only_possible_number assumed false
                only_possible_number = False
                # We want to save after validate is true. So that we can put that
                # into the puzzle.
                number_selected = 0

                for number in range(1, 10):
                    if only_possible_number is True:
                        temp = validate(puzzle, row, row_number, column_number, number)
                        if temp is True:
                            only_possible_number = False
                            break
                    else:
                        only_possible_number = validate(puzzle, row, row_number, column_number, number)
                        # We want to save the number once we
                        if only_possible_number is True:
                            number_selected = number

                if only_possible_number is True:
                    puzzle[row_number][column_number] = number_selected
                # print('There is only one number possible: {}'.format(number_selected))

    return puzzle



# Takes individual entry value and determines if it is valid entry returns bool
def validate(puzzle, row, row_number, column_number, value):
    column = getcolumn(puzzle, column_number)
    box = getbox(puzzle, column_number, row_number)
    # already have row so, just use it

    if value not in row and value not in column and value not in box:
        return True
    else:
        return False

# Provided an x and y coordinates, returns an array of the small box to which it belongs.
# def getboxcoordinates(x, y):
#     boxColumn = int(x/3)
#     boxRow = int(y/3)
#     print(boxColumn, boxRow)
#     return boxRow, boxColumn


# Helper function to grab the box from an index and return that box as an array,
# since we can't use the arrays like we do in each of the rows.
def getbox(puzzle, column_number, row_number):
    row_start_position = row_number // 3 * 3
    column_start_position = column_number // 3 * 3

    box = []
    for i in range(3):
        for j in range(3):
            box.append(puzzle[row_start_position+i][column_start_position+j])

    return box


# Helper function to grab the column from an index and return that box as an array,
# since we can't use the arrays like we do in each of the rows.
def getcolumn(puzzle, index):
    array = []
    for i in range(9):
        array.append(puzzle[i][index])
    return array


main()
