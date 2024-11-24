def is_valid_grid(grid):
    
    def has_duplicates(sequence):
        nums = [x for x in sequence if x != 0]
        return len(nums) != len(set(nums))

    # Check rows and columns
    for i in range(9):
        if has_duplicates(grid[i]) or has_duplicates([grid[j][i] for j in range(9)]):
            return False

    # Check 3x3 subgrids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = [
                grid[row + i][col + j]
                for i in range(3)
                for j in range(3)
            ]
            if has_duplicates(subgrid):
                return False

    return True


def is_safe(grid, row, col, num):
    
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(grid):
    
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num

                        if solve_sudoku(grid):
                            return True

                        grid[row][col] = 0  # Backtrack

                return False  # No valid number found

    return True


def print_grid(grid):
    
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


if __name__ == "__main__":
    sudoku_grid = [
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [1, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 7, 0, 0],
    [0, 0, 0, 1, 0, 2, 0, 0, 0],
    [0, 0, 6, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 1],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    print("Original Sudoku grid:")
    print_grid(sudoku_grid)

    if is_valid_grid(sudoku_grid):
        if solve_sudoku(sudoku_grid):
            print("\nSolved Sudoku grid:")
            print_grid(sudoku_grid)
        else:
            print("\nNo solution exists for the given Sudoku grid.")
    else:
        print("\nInvalid Sudoku grid.")
