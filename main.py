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
    for row in puzzle:
        for index in range(len(row)):
            if row[index] == 0:
                checkRow(row)
                checkColumn(index, puzzle)
                checkBox()

            print('This is index {} with value {}'.format(index, row[index]))
            # if value == 0:
            #     print('This row {} at this value {}'.format(row, value))


def checkRow(row):
    for index in range(len(row)):
        if index not in row:
            return True
    return False

# if __name__ == '__main__':
main()

