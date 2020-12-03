with open("3_toboggan_trajectory_input.txt") as f:
    grid = f.read()

grid = grid.split("\n")

del grid[-1]  # remove new line


def wrap(n, min_, max_):
    return (n - min_) % (max_ - min_) + min_


slope_hits = []

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
for slope in slopes:
    toboggan = [0, 0]
    trees_hit = 0
    while True:
        if toboggan[1] >= len(grid):
            break
        if grid[toboggan[1]][toboggan[0]] == "#":
            trees_hit += 1
        toboggan[0] = wrap(toboggan[0] + slope[0], 0, len(grid[0]))
        toboggan[1] = toboggan[1] + slope[1]
    slope_hits.append(trees_hit)

print("Slope Hits:", slope_hits)

total = 1
for slope in slope_hits:
    total *= slope

print(total)
