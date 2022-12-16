#Day 4: Camp Cleanup

def check_section(section):
    range_1_start = int(section[0][0])
    range_1_end = int(section[0][1])

    range_2_start = int(section[1][0])
    range_2_end = int(section[1][1])

    set_1 = set(range(range_1_start, range_1_end + 1))
    set_2 = set(range(range_2_start, range_2_end + 1))

    if set_1.intersection(set_2):
        return True
    elif set_2.intersection(set_1):
        return True
    else:
        return False

if __name__ == '__main__':
    f = open("day_4_input.txt")

    contents = f.read().split("\n")

    print(contents)

    list_a = []
    for i in contents:
        x = i.split(",")
        list_a.append(x)
    print(list_a)
    list_b = []
    final_list = []
    for i in list_a:
        list_b = []
        for j in i:
            x = j.split("-")
            list_b.append(x)
        final_list.append(list_b)
    print(final_list)

    count = 0

    for i in final_list:

        if check_section(i):
            count += 1





    print(count)