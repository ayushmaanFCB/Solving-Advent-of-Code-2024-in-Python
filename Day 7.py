from pprint import pprint


def read_data():
    required = {}
    with open("data/day_7_input.txt", "r") as file:
        datas = file.read().split("\n")
        for data in datas:
            temp = data.split(": ")
            if temp != [""]:
                required.update({int(temp[0]): list(map(int, temp[1].split(" ")))})
    # print(len(required))
    return required


# PART 1
def valid_calibration_eqn(
    data={
        190: [10, 19],
        3267: [81, 40, 27],
        83: [17, 5],
        156: [15, 6],
        7290: [6, 8, 6, 15],
        161011: [16, 10, 13],
        192: [17, 8, 14],
        21037: [9, 7, 18, 13],
        292: [11, 6, 16, 20],
    }
):
    def can_evaluate(numbers, target, index, current_value):
        if index == len(numbers):
            return current_value == target

        return can_evaluate(
            numbers, target, index + 1, current_value + numbers[index]
        ) or can_evaluate(numbers, target, index + 1, current_value * numbers[index])

    total_calibration_result = 0

    for target, numbers in data.items():
        if can_evaluate(numbers, target, 1, numbers[0]):
            total_calibration_result += target

    return total_calibration_result


if __name__ == "__main__":
    required = read_data()
    print("TOTAL CALIBRATION RESULT : ", valid_calibration_eqn(required))
