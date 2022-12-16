#Day 5: Supply Stacks

f = open("day_5_input.txt")

contents = f.readlines()


stacks = []


for i in contents:

    stacks.append(i)


    if i[1] == "1":
         break

stacks.reverse()
compiled_stacks = []

for i in stacks[0]:
        if i.isspace():
            pass
        else:
            i_index = stacks[0].index(i)
            stack = []
            for j in range(1,len(stacks)):
                if stacks[j][i_index].isspace():
                    break
                stack.append(stacks[j][i_index])
            compiled_stacks.append(stack)



commands = []
for i in contents:
    if i[0]== "m":
        commands.append(i)



shortened_commands = []

for i in commands:
    command = []
    for j in i:
        if j.isdigit():
            command.append(j)
        elif j.isspace():
            command.append(j)
        else:
            pass
    shortened_commands.append(command)


final_command_list = []

for i in shortened_commands:
    check = False
    command = []
    for j in range(0,len(i)):
        if check:
            check = False
            continue
        if j != len(i)-1:
            if i[j].isdigit() and i[j+1]:
                command.append(int(i[j]+i[j+1]))
                check = True
        if not check:
            if i[j].isdigit():
                command.append(int(i[j]))
    final_command_list.append(command)


for i in final_command_list:

    if i[0] > len(compiled_stacks[i[1]-1]):
        range_value = len(compiled_stacks[i[1]-1])
    else:
        range_value = i[0]

    for j in range(0, range_value):
        compiled_stacks[i[2]-1].append(compiled_stacks[i[1]-1][j- range_value])
    for j in range(0, range_value):
        del compiled_stacks[i[1]- 1][-1]



#answer
for i in range(0, len(compiled_stacks)):
    if len(compiled_stacks[i]) != 0:
        print(f"{compiled_stacks[i][-1]}", end="")