def generate():
    puzzle1 = [
        [0, 4, 0, 0, 2, 0, 1, 7, 0],
        [7, 0, 6, 0, 5, 0, 9, 0, 3],
        [0, 0, 0, 0, 7, 3, 6, 0, 2],
        [4, 0, 9, 0, 0, 5, 2, 0, 0],
        [1, 0, 0, 7, 0, 0, 0, 9, 0],
        [5, 0, 8, 2, 1, 0, 4, 0, 0],
        [9, 1, 0, 0, 0, 8, 0, 0, 4],
        [0, 8, 0, 0, 4, 2, 5, 0, 0],
        [2, 0, 4, 0, 9, 7, 3, 0, 0]
    ]

    array = [[i+1 for i in range(9)] for j in range(9)]
    return puzzle1


# samplePuzzle = generate()
# for arr in samplePuzzle:
#     print(arr)
