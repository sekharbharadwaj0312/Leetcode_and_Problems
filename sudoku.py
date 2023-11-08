def is_valid(grid):
    for i in range(9):
        row_set = set()
        col_set = set()
        for j in range(9):
            if grid[i][j] != 0 and grid[i][j] in row_set:
                return False
            row_set.add(grid[i][j])
            if grid[j][i] != 0 and grid[j][i] in col_set:
                return False
            col_set.add(grid[j][i])

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            submatrix_set = set()
            for x in range(3):
                for y in range(3):
                    if grid[i + x][j + y] != 0 and grid[i + x][j + y] in submatrix_set:
                        return False
                    submatrix_set.add(grid[i + x][j + y])

    return True

def solve_sudoku(grid, numbers, K):
    wrong_cells = []

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:  # Empty cell
                original_value = grid[i][j]
                for num in numbers:
                    grid[i][j] = num
                    if is_valid(grid):
                        break
                else:
                    wrong_cells.append((i, j))
                grid[i][j] = original_value  # Reset the grid for the next iteration

    if len(wrong_cells) == 0:
        print("Won")
    elif len(wrong_cells) > K:
        print("Impossible")
    else:
        for cell in wrong_cells:
            print(cell[0], cell[1])

# Read input
grid = [list(map(int, input().split())) for _ in range(9)]
numbers = list(map(int, input().split()))
K = int(input())

# Solve Sudoku and print the result
solve_sudoku(grid, numbers, K)
