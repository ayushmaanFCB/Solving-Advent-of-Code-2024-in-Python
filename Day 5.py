from pprint import pprint


# Separates and Organizes the input into Rules (Example can be seen in the funciton signature) and Updates
def read_data():
    with open("./data/day_5_input.txt", "r") as file:
        lines = file.readlines()

    rules = {}
    updates = []

    for line in lines:
        line = line.strip()
        if "|" in line:
            key, value = map(int, line.split("|"))
            if key in rules:
                rules[key].append(value)
            else:
                rules[key] = [value]
        elif line:
            numbers = list(map(int, line.split(",")))
            updates.append(numbers)
    return rules, updates


def sum_correct_rules(updates):
    ssum = 0
    for update in updates:
        ssum += update[len(update) // 2]
    return ssum


# PART 1
def rule_validator(
    rules={
        47: [53, 13, 61, 29],
        97: [13, 61, 47, 29, 53, 75],
        75: [29, 53, 47, 61, 13],
        61: [13, 53, 29],
        29: [13],
        53: [29, 13],
    },
    updates=[
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ],
):
    valid_rules, invalid_rules = [], []
    for update in updates:
        flag = True
        for i, data in enumerate(update):
            if i != len(update) - 1:
                if data not in rules:
                    flag = False
                    continue
                fetched_rule = rules[data]
                for num in update[i + 1 :]:
                    if num in fetched_rule:
                        continue
                    else:
                        flag = False
                        break
        if flag:
            valid_rules.append(update)
        else:
            invalid_rules.append(update)

    return valid_rules, invalid_rules


# PART 2
def reorder_incorrect_updates(
    rules={
        47: [53, 13, 61, 29],
        97: [13, 61, 47, 29, 53, 75],
        75: [29, 53, 47, 61, 13],
        61: [13, 53, 29],
        29: [13],
        53: [29, 13],
    },
    updates=[
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ],
):
    def reorder(update):
        sorted_update = []
        for page in update:
            if not sorted_update:
                sorted_update.append(page)
            else:
                inserted = False
                for i, existing_page in enumerate(sorted_update):
                    if page in rules and existing_page in rules[page]:
                        sorted_update.insert(i, page)
                        inserted = True
                        break
                if not inserted:
                    sorted_update.append(page)
        return sorted_update

    valid_updates, invalid_updates = rule_validator(rules, updates)
    fixed_updates = [reorder(update) for update in invalid_updates]

    return fixed_updates


if __name__ == "__main__":
    rules, updates = read_data()

    # PART 1
    valid_updates, _ = rule_validator(rules, updates)
    print("SUM OF ALL VALID MIDDLE ELEMENTS: ", sum_correct_rules(valid_updates))

    # PART 2
    fixed_updates = reorder_incorrect_updates(rules, updates)
    print("SUM OF MIDDLE ELEMENTS OF FIXED UPDATES: ", sum_correct_rules(fixed_updates))
