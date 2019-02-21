import numpy


def solve_sudoku(num):
    numbers = num.copy()
    squares = numpy.array(
        [
            [0, 1, 2, 9, 10, 11, 18, 19, 20],
            [3, 4, 5, 12, 13, 14, 21, 22, 23],
            [6, 7, 8, 15, 16, 17, 24, 25, 26],
            [27, 28, 29, 36, 37, 38, 45, 46, 47],
            [30, 31, 32, 39, 40, 41, 48, 49, 50],
            [33, 34, 35, 42, 43, 44, 51, 52, 53],
            [54, 55, 56, 63, 64, 65, 72, 73, 74],
            [57, 58, 59, 66, 67, 68, 75, 76, 77],
            [60, 61, 62, 69, 70, 71, 78, 79, 80]
        ]
    )
    possible_numbers = list()
    possible_numbers_length_tw = list()
    for i in range(0, 9):
        for j in range(0, 9):
            index = 9 * i + j
            possible_numbers.append([])
            number_of_square = numpy.where(squares == (9*i+j))
            possible_numbers[index] = find_possible_numbers(numbers, i, j, squares[number_of_square[0][0]])
            if len(possible_numbers[index]) == 2:
                possible_numbers_length_tw.append(index)
            if numbers[i][j] == 0 and len(possible_numbers[index]) == 0:
                return False

    possible_numbers = numpy.array(possible_numbers)
    for i in range(0, 9):
        counts = numpy.zeros(9)
        for j in range(0, 9):
            for k in possible_numbers[squares[i][j]]:
                counts[k-1] += 1
            number_of_square = numpy.where(squares == (9 * i + j))
            p = find_possible_numbers(numbers, i, j, squares[number_of_square[0][0]])
            if len(p) == 1:
                numbers[squares[i][j] // 9][squares[i][j] % 9] = p[0]
                possible_numbers[squares[i][j]] = []
        indices = numpy.where(counts == 1)
        if len(indices[0]) > 0:
            for j in range(0, 9):
                for k in indices[0]:
                    if k+1 in possible_numbers[squares[i][j]]:
                        numbers[squares[i][j]//9][squares[i][j] % 9] = k+1
                        possible_numbers[squares[i][j]] = []
    cn = numpy.where(sum(numbers) < 45)
    if len(cn[0]) > 0:
        print(numbers)
        if numpy.alltrue(num == numbers):
            for e in possible_numbers_length_tw:
                for f in possible_numbers[e]:
                    numbers[e // 9][e % 9] = f
                    possible_numbers[e] = []
                    solve_sudoku(numbers)
                    numbers = num.copy()
        numbers = solve_sudoku(numbers)
    return numbers


def find_possible_numbers(numbers, i, j, squares):
    possible_numbers = []
    if numbers[i][j] == 0:
        rows = numbers[i, numpy.where(numbers[i, ] > 0)]
        cols = numbers[numpy.where(numbers[:, j] > 0), j]
        square_number = list()
        for l in range(9):
            row = squares[l] // 9
            col = squares[l] % 9
            if numbers[row][col] > 0:
                square_number.append(numbers[row][col])
        square_number = numpy.array(square_number)
        x = numpy.array(range(1, 10))
        t = numpy.unique(numpy.concatenate((rows, cols, square_number), axis=None))
        possible_numbers = numpy.delete(x, t - 1).tolist()
    return possible_numbers


num = numpy.array([
    [0, 0, 4, 0, 3, 0, 0, 0, 0],
    [0, 1, 0, 8, 0, 0, 7, 3, 0],
    [0, 0, 0, 0, 1, 0, 0, 9, 6],
    [4, 0, 0, 0, 0, 9, 0, 7, 0],
    [0, 3, 0, 0, 0, 0, 0, 4, 0],
    [0, 5, 0, 1, 0, 0, 0, 0, 8],
    [3, 8, 0, 0, 9, 0, 0, 0, 0],
    [0, 4, 1, 0, 0, 2, 0, 8, 0],
    [0, 0, 0, 0, 5, 0, 2, 0, 0]
])

v = solve_sudoku(num)
print(v)