def read_data():
    with open("./data/day_4_input.txt", "r") as file:
        text = file.readlines()
        text = [t.strip("\n") for t in text]
    return text


def count_word_occurrences(
    grid=[
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ],
    word="XMAS",
):
    def search_from_position(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                return False
            if grid[nx][ny] != word[i]:
                return False
        return True

    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1),
    ]

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if search_from_position(x, y, dx, dy):
                    count += 1

    return count


def count_xmas_patterns(
    grid=[
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
):
    ret = 0

    def check_xmas_x_shape(x: int, y: int) -> bool:
        if grid[x][y] != "A":
            return False

        top_left = (grid[x - 1][y - 1], grid[x + 1][y + 1])
        top_right = (grid[x - 1][y + 1], grid[x + 1][y - 1])

        return top_left in {("M", "S"), ("S", "M")} and top_right in {
            ("M", "S"),
            ("S", "M"),
        }

    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            if check_xmas_x_shape(x, y):
                ret += 1

    return ret


if __name__ == "__main__":
    print("Occurences of XMAS : ", count_word_occurrences(read_data()))
    print("Occurences of Valid X - MAS : ", count_xmas_patterns(read_data()))
