from collections import deque


def read_data():
    with open("data/day_18_input.txt") as file:
        data = file.readlines()
        final_data = []
        for line in data:
            line = line.strip("\n")
            final_data.append((int(line.split(",")[0]), int(line.split(",")[1])))

    return final_data


# PART 1
def minimum_steps_to_exit(
    grid_size=7,
    byte_positions=[
        (5, 4),
        (4, 2),
        (4, 5),
        (3, 0),
        (2, 1),
        (6, 3),
        (2, 4),
        (1, 5),
        (0, 6),
        (3, 3),
        (2, 6),
        (5, 1),
        (1, 2),
        (5, 5),
        (2, 5),
        (6, 5),
        (1, 4),
        (0, 4),
        (6, 4),
        (1, 1),
        (6, 1),
        (1, 0),
        (0, 5),
        (1, 6),
        (2, 0),
    ],
    max_bytes=12,
):
    n = grid_size
    grid = [["." for _ in range(n)] for _ in range(n)]

    for idx, (x, y) in enumerate(byte_positions[:max_bytes]):
        grid[y][x] = "#"

    start = (0, 0)
    end = (n - 1, n - 1)

    if grid[0][0] == "#" or grid[end[1]][end[0]] == "#":
        return -1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque([(0, 0, 0)])
    visited = set()
    visited.add((0, 0))

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < n
                and (nx, ny) not in visited
                and grid[ny][nx] == "."
            ):
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1


if __name__ == "__main__":
    steps = minimum_steps_to_exit(
        grid_size=71, byte_positions=read_data(), max_bytes=1024
    )
    print(f"Minimum steps to exit: {steps}")
