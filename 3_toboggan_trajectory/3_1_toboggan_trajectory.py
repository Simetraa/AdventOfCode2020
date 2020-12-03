with open("3_toboggan_trajectory_input.txt") as f:
    grid = f.read()

grid = grid.split("\n")

del grid[-1]  # remove new line


def wrap(n, min_, max_):
    return (n - min_) % (max_ - min_) + min_


toboggan = [0, 0]

trees_hit = 0
while True:
    if toboggan[1] >= len(grid):
        break
    if grid[toboggan[1]][toboggan[0]] == "#":
        trees_hit += 1

    toboggan[0] = wrap(toboggan[0] + 3, 0, len(grid[0]))
    toboggan[1] = toboggan[1] + 1


print("Trees hit:", trees_hit)
