def reach_end(pos, maxx, maxy):
    return pos[0] == 0 or pos[0] == maxx - 1 or pos[1] == 0 or pos[1] == maxy - 1


next_dir = {"^": [0, -1], "v": [0, 1], "<": [-1, 0], ">": [1, 0]}

next_guard = {"^": ">", "v": "<", "<": "^", ">": "v"}


def parse_input():
    with open("data/day_6_input.txt", "r") as file:
        data = [list(line) for line in file.read().splitlines()]

    maxy = len(data)
    maxx = len(data[0])
    guard = ["^", "v", "<", ">"]

    start = []
    for yi in range(maxy):
        for xi in range(maxx):
            if data[yi][xi] in guard:
                start = [xi, yi]
                break
        if start:
            break

    return data, start, maxx, maxy


def move(pos, dir, data, maxx, maxy, result):
    nx, ny = pos[0], pos[1]
    gx, gy = nx, ny

    while True:
        if data[ny][nx] == "#":
            return gx, gy
        result.add(f"{nx}_{ny}")
        if reach_end([nx, ny], maxx, maxy):
            data[ny][nx] = "X"
            return nx, ny
        gx, gy = nx, ny
        data[gy][gx] = "X"
        nx += dir[0]
        ny += dir[1]


def part1():
    data, start, maxx, maxy = parse_input()
    result = set()

    def game():
        gx, gy = start[0], start[1]
        gua = data[gy][gx]
        while not reach_end([gx, gy], maxx, maxy):
            dir = next_dir.get(gua)
            gx, gy = move([gx, gy], dir, data, maxx, maxy, result)
            gua = next_guard.get(gua)

    game()
    print(len(result))


def part2():
    data, start, maxx, maxy = parse_input()
    data[start[1]][start[0]] = "^"

    possibilities = []
    count_obstacles = 0

    for yi in range(maxy):
        for xi in range(maxx):
            if data[yi][xi] == "X":
                possibilities.append([xi, yi])
            if data[yi][xi] == "#" and yi < maxy - 1 and xi < maxx - 1:
                count_obstacles += 1

    max_moves = ((maxx - 2) * (maxy - 2)) - count_obstacles

    def move2(pos, dir, data):
        nx, ny = pos[0], pos[1]
        gx, gy = nx, ny
        steps = 0
        while True:
            if data[ny][nx] == "#":
                steps -= 1
                return gx, gy, steps
            if reach_end([nx, ny], maxx, maxy):
                data[ny][nx] = "X"
                return nx, ny, steps
            gx, gy = nx, ny
            data[gy][gx] = "X"
            nx += dir[0]
            ny += dir[1]
            steps += 1

    def check_loop():
        history = {}
        gx, gy = start[0], start[1]
        gua = data[gy][gx]
        count = 0
        while not reach_end([gx, gy], maxx, maxy):
            dir = next_dir.get(gua)
            gx, gy, steps = move2([gx, gy], dir, data)
            gua = next_guard.get(gua)
            count += steps
            if ((gx, gy) in history and history[(gx, gy)] == gua) or count > max_moves:
                return True
            history[(gx, gy)] = gua
        return False

    loop_count = 0
    for obstacle in possibilities:
        data[start[1]][start[0]] = "^"
        provx, provy = obstacle[0], obstacle[1]
        data[provy][provx] = "#"
        if check_loop():
            loop_count += 1
        data[provy][provx] = "X"

    print(loop_count)


if __name__ == "__main__":
    part1()
    part2()
