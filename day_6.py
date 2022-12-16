f = open("day_6_input.txt")

contents = f.read()

print(contents)

end_loop = True
for i in range(14, len(contents)):
    if not end_loop:
        break
    section = contents[i-14:i]

    total = 0
    for j in section:
        counts = section.count(j)
        total += counts
    if total < 15:

        first_marker = i
        print(first_marker)
        end_loop = False

