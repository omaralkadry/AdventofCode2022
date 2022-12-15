#Day 2: Rock Paper Scissors

f = open("day_2_input.txt")

contents = f.read().split("\n")

print(contents)

#Part 2: X is lose, Y is draw, Z is win
#A is Rock, B is Paper, and C is Scissors
#Rock = 1, Paper = 2, Scissors = 3
def calculate_score(opponent, you):
    score = 0
    if you == "X":
        score += 0
        if opponent == "A":
            score += 3
        elif opponent == "B":
            score += 1
        elif opponent == "C":
            score += 2
    elif you == "Y":
        score += 3
        if opponent == "A":
            score += 1
        elif opponent == "B":
            score += 2
        elif opponent == "C":
            score += 3
    elif you == "Z":
        score += 6
        if opponent == "A":
            score += 2
        elif opponent == "B":
            score += 3
        elif opponent == "C":
            score += 1

    return score

total_score = 0
for i in range (0, len(contents)):

    calculated_score = calculate_score(contents[i][0], contents[i][2])
    total_score += calculated_score

print(total_score)
