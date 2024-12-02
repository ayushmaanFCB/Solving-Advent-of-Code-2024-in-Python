from pprint import pprint


def read_data():
    with open("./data/day_2_input.txt", "r") as file:
        datas = file.readlines()

    required_ = []
    for data in datas:
        new = data.strip("\n").split(" ")
        new = list(map(int, new))
        required_.append(new)
    return required_


def safety_checker(
    levels=[
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
):
    counter = 0
    for level in levels:
        is_increasing = all(
            1 <= level[i + 1] - level[i] <= 3 for i in range(len(level) - 1)
        )
        is_decreasing = all(
            1 <= level[i] - level[i + 1] <= 3 for i in range(len(level) - 1)
        )
        if is_increasing or is_decreasing:
            counter += 1
    return counter


def appended_safety_checker(
    levels=[
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
):
    def is_safe(level):
        is_increasing = all(
            1 <= level[i + 1] - level[i] <= 3 for i in range(len(level) - 1)
        )
        is_decreasing = all(
            1 <= level[i] - level[i + 1] <= 3 for i in range(len(level) - 1)
        )
        return is_increasing or is_decreasing

    counter = 0
    for level in levels:
        if is_safe(level):
            counter += 1
        else:
            for i in range(len(level)):
                modified_level = level[:i] + level[i + 1 :]
                if is_safe(modified_level):
                    counter += 1
                    break
    return counter


if __name__ == "__main__":
    print("SAFE LEVELS: ", safety_checker(read_data()))
    print("DAMPENED SAFE LEVELS: ", appended_safety_checker(read_data()))
