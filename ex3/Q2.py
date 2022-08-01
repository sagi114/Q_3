def solve(matrix):
    row=len(matrix)
    col = len(matrix)
    for r in range(row):
        act_row = row-r-1
        if act_row == 0:
            return matrix[act_row][0]
        for c in range(col-1-r):
            matrix[act_row-1][c] += max(matrix[act_row][c],matrix[act_row][c+1])
if __name__ == '__main__':
    matrix=[
        [3, 0, 0, 0],
        [7, 4, 0, 0],
        [2, 4, 6, 0],
        [8, 5, 9, 3]
    ]
    print(solve(matrix))
    matrix = [
        [8, 0, 0, 0],
        [4, 4, 0, 0],
        [2, 2, 6, 0],
        [1, 1, 1, 1]
    ]
    print(solve(matrix))