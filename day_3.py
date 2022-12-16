#Day 3: Rucksack Reorganization

f = open("day_3_input.txt")

contents = f.read().split("\n")

print(contents)

def find_letter(index):
    for i in contents[index]:
        for j in contents[index + 1]:
            if i == j:
                for k in contents[index + 2]:
                    if i == k:
                        return i

def calculate_value(character):
    number = ord(character)
    if 97 <= number <= 122:
        calculated_number = number - 96
    elif 65 <= number <= 90:
        calculated_number = number -38
    else:
        calculated_number = None

    return calculated_number

total_sum = 0
for a in range(0, len(contents), 3):
    common_letter = find_letter(a)
    value = calculate_value(common_letter)
    total_sum += value

print(total_sum)

