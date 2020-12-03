with open('day1\input.txt') as file:
    numbers = [int(line.rstrip()) for line in file]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if (numbers[i] + numbers[j]) == 2020:
            print("Two Sum:", numbers[i] * numbers[j])

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1, len(numbers)):
            if (numbers[i] + numbers[j] + numbers[k]) == 2020:
                print("Three Sum:", numbers[i] * numbers[j] * numbers[k])
