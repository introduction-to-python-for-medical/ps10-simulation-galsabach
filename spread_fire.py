def spread_fire(grid, grid_size):
    """Update the forest grid based on fire spreading rules."""
    new_grid = copy.deepcopy(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
                neighbors = []
                # Check all valid neighbors
                if i > 0: neighbors.append(grid[i - 1][j])
                if i < grid_size - 1: neighbors.append(grid[i + 1][j])
                if j > 0: neighbors.append(grid[i][j - 1])
                if j < grid_size - 1: neighbors.append(grid[i][j + 1])
                
                if 2 in neighbors:
                    new_grid[i][j] = 2
    return new_grid

# Set up the grid
grid_size = 30
p_tree = 0.6

grid = initialize_forest(grid_size, p_tree)

# Run the simulation
fig, ax = plt.subplots()
for i in range(100):
    grid = spread_fire(grid, grid_size)
    ax.imshow(grid, cmap='YlOrRd', vmin=0, vmax=2)
    ax.set_title(f'Step {i}')
    display(fig)
    clear_output(wait=True)
    plt.pause(0.01)
