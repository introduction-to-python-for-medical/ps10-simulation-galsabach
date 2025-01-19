def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    update_grid = copy.deepcopy(grid)
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                neighbors = []
                # Check all valid neighbors
                if i > 0: neighbors.append(grid[i-1][j])
                if i < rows - 1: neighbors.append(grid[i+1][j])
                if j > 0: neighbors.append(grid[i][j-1])
                if j < cols - 1: neighbors.append(grid[i][j+1])

                if 2 in neighbors:
                    update_grid[i][j] = 2
    return update_grid
