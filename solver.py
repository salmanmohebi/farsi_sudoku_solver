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
    possible_numbers = find_possible_numbers(numbers, squares)
    if possible_numbers:
        possible_numbers = numpy.array(possible_numbers)
        for i in range(0, 9):
            counts = numpy.zeros(9)
            for j in range(0, 9):
                for k in possible_numbers[squares[i][j]]:
                    counts[k-1] += 1
                    if len(possible_numbers[squares[i][j]]) == 1:
                        numbers[squares[i][j] // 9][squares[i][j] % 9] = possible_numbers[squares[i][j]][0]
                        possible_numbers[squares[i][j]] = []
            indices = numpy.where(counts == 1)
            if len(indices[0]) > 0:
                for j in range(0, 9):
                    for k in indices[0]:
                        if k+1 in possible_numbers[squares[i][j]]:
                            numbers[squares[i][j]//9][squares[i][j] % 9] = k+1
                            possible_numbers[squares[i][j]] = []
        if numpy.alltrue(num == numbers):
            for i in range(0, 9):
                counts = numpy.zeros(9)
                for j in range(0, 9):
                    for k in possible_numbers[squares[i][j]]:
                        counts[k - 1] += 1
                indices = numpy.where(counts == 2)
                if len(indices[0]) > 0:
                    for j in range(0, 9):
                        k = indices[0][0]
                        if k + 1 in possible_numbers[squares[i][j]]:
                            numbers[squares[i][j] // 9][squares[i][j] % 9] = k + 1
                            possible_numbers[squares[i][j]] = []
                            numbers = solve_sudoku(numbers)
                            cn = numpy.where(sum(numbers) < 45)
                            if len(cn[0]) > 0:
                                numbers = num.copy()
                            else:
                                return numbers
        else:
            numbers = solve_sudoku(numbers)
    return numbers


def find_possible_numbers(numbers, squares):
    possible_numbers = list()
    for i in range(0, 9):
        for j in range(0, 9):
            index = 9 * i + j
            possible_numbers.append([])
            if numbers[i][j] == 0:
                rows = numbers[i, numpy.where(numbers[i, ] > 0)]
                cols = numbers[numpy.where(numbers[:, j] > 0), j]
                number_of_square = numpy.where(squares == (9 * i + j))
                square = squares[number_of_square[0][0]]
                square_number = list()
                for l in range(9):
                    row = square[l] // 9
                    col = square[l] % 9
                    if numbers[row][col] > 0:
                        square_number.append(numbers[row][col])
                square_number = numpy.array(square_number)
                x = numpy.array(range(1, 10))
                t = numpy.unique(numpy.concatenate((rows, cols, square_number), axis=None))
                u = numpy.delete(x, t - 1).tolist()
                possible_numbers[index] = u
                if len(u) ==0:
                    return False
    return possible_numbers


num = numpy.array([
    [0, 7, 4, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 2, 1, 0, 6, 0, 0],
    [0, 1, 0, 5, 0, 0, 0, 0, 0],
    [0, 8, 2, 0, 5, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 6, 0, 7, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 6, 0, 1, 0],
    [0, 0, 7, 0, 2, 8, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 7, 3, 0]
])
v = solve_sudoku(num)
print(v)
