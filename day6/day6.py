with open('day6/input.txt') as file:
    lines = file.readlines()

total_count = 0
answers = set()
for line in lines:
    if line.isspace():
        total_count += len(answers)
        answers = set()
        continue
    for q in line.strip():
        answers.add(q)
print("# where anyone answered yes: ", total_count)

total_count = 0
answers = {}
num_in_group = 0
for line in lines:
    if line.isspace():
        for key in answers:
            if answers[key] == num_in_group:
                total_count += 1
        answers = {}
        num_in_group = 0
        continue
    num_in_group += 1
    for q in line.strip():
        if q not in answers:
            answers[q] = 1
        else:
            answers[q] = answers[q] + 1
        
print("# where everyone answered yes: ", total_count)
    