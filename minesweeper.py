# This program takes in a 2D list input, which represents a grid of cells. Each cell is either a mine ("#"), or it is not ("-").
# The program then creates a new grid where each cell contains a count of how many mines are in neighboring cells.
# The program first determines the number of rows and columns in the input grid. It then creates a new empty grid new_grid. 
# The program then iterates over each row and column in the input grid using nested loops and enumerate function.
# The program counts the number of neighboring mines using two nested loops that iterate over the neighboring cells.
# The loops use max and min to ensure that the indices of the neighboring cells do not go out of bounds.

def count_mines(input):
    n_rows = len(input)
    n_cols = len(input[0])
    new_grid = []
    for i, row in enumerate(input):
        new_row = []
        for j, cell in enumerate(row):
            if cell == "-":
                count = 0
                for a in range(max(0, i-1), min(n_rows, i+2)):
                    for b in range(max(0, j-1), min(n_cols, j+2)):
                        if input[a][b] == "#":
                            count += 1
                new_row.append(str(count))
            else:
                new_row.append(cell)
        new_grid.append(new_row)
    return new_grid

input = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]

# Function count-mines is called and output printed.

output = count_mines(input)
print(output)





