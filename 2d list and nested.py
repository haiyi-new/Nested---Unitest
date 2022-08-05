number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]                            # Create grid like to the python
]

print(number_grid[0][0])
print(number_grid[0][1])
print(number_grid[2][1])  # It read row(up to down), then column(left to right)

# Nested for loop
for row in number_grid:
    for column in row:
        print(column)
for row in number_grid:
    print(row)
    