import re

with open('day2\input.txt') as file:
    passwords = [line.rstrip() for line in file]
total_valid = 0
for line in passwords:
    match = re.search('(\d+)-(\d+)\s+([a-zA-Z]):\s+([a-zA-Z]+)', line)
    min_value = int(match.group(1))
    max_value = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)
    if min_value <= password.count(letter) <= max_value:
        total_valid += 1
print("Total Valid: ", total_valid)


total_valid = 0
for line in passwords:
    match = re.search('(\d+)-(\d+)\s+([a-zA-Z]):\s+([a-zA-Z]+)', line)
    first_pos = int(match.group(1))
    second_pos = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)
    if bool(password[first_pos - 1] == letter) != bool(password[second_pos - 1] == letter):
        total_valid += 1
print("Total Valid: ", total_valid)
