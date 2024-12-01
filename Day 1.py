def read_data():
    with open("./data/day_1a_input.txt", "r") as file:
        datas = file.readlines()

    list1, list2 = [], []
    for data in datas:
        data = str(data).split("   ")
        list1.append(int(data[0]))
        list2.append(int(data[1].strip("\n")))

    print(f"List 1: {len(list1)} elements; List 2: {len(list2)} elements")
    return list1, list2

def compare_list_by_min(list1=[3,4,2,1,3,3], list2=[4,3,5,3,9,3]):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    
    pairs = list(zip(sorted_list1, sorted_list2))
    differences = [abs(a - b) for a, b in pairs]
    
    return sum(differences)

def compare_list_by_occurences(list1=[3,4,2,1,3,3], list2=[4,3,5,3,9,3]):
    occurences = []
    for num1 in list1:
        count = 0
        for num2 in list2:
            if num1 == num2:
                count += 1
        occurences.append(num1*count)
    return sum(occurences)

if __name__ == '__main__':
    list1, list2 = read_data()
    result1 = compare_list_by_min(list1=list1, list2=list2)
    print("BY MINIMUMUM = ",result1)

    result2 = compare_list_by_occurences(list1=list1, list2=list2)
    print("BY OCCURENCES = ", result2)


