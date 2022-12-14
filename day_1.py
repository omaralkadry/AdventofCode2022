#Day 1: Calorie Counting

f = open("day_1_input.txt")

contents = f.read().split("\n")

print(contents)

stacks = []
stack_list = []

for i in contents:
    if i == "":
        stack_list.append(stacks)
        stacks = []
    if i != "":
        stacks.append(int(i))

print(stack_list)

sum_list = []

for i in stack_list:
    sum_list.append(sum(i))

print(sum_list)

max_value = max(sum_list)
print(max_value)

first = 0
second = 0
third = 0
for i in sum_list:
    if i > first:
        third = second
        second = first
        first = i
    elif i > second:
        third = second
        second = i
    elif i > third:
        third = i

print(first + second + third)