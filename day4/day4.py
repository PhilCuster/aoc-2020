import re
'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
'''

tracker = {
    'byr': False,
    'iyr': False,
    'eyr': False,
    'hgt': False,
    'hcl': False,
    'ecl': False,
    'pid': False,
    'cid': False
}
valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validatevalue(value):
    key = value[0]
    if key == 'cid':
        return True
    if key == 'byr':
        return 1920 <= int(value[1]) <= 2002
    if key == 'iyr':
        return 2010 <= int(value[1]) <= 2020
    if key == 'eyr':
        return 2020 <= int(value[1]) <= 2030
    if key == 'hgt':
        match = re.search('(\d+)(\D+)', value[1])
        if match == None:
            return False
        if match.group(2) == 'cm':
            return 150 <= int(match.group(1)) <= 193
        if match.group(2) == 'in':
            return 59 <= int(match.group(1)) <= 76
    if key == 'hcl':
        return re.fullmatch('#([0-9a-f]{6})', value[1]) != None
    if key == 'ecl':
        return value[1] in valid_eye_colors
    if key == 'pid':
        return re.fullmatch('[0-9]{9}', value[1]) != None
    return False

def resettracker():
    for key in tracker:
        tracker[key] = False

def evaluatetracker():
    for key in tracker:
        if key != 'cid' and not tracker[key]:
            return False
    return True

num_correct = 0

with open('day4/input.txt') as file:
    num = 0
    for line in file:
        num +=1
        if line.isspace():
            if evaluatetracker():
                num_correct += 1
            resettracker()
            continue
        match = re.findall('(?:^|\s+)(\w+):(\S+)', line)
        for s in match:
            tracker[s[0]] = validatevalue(s)


print("Valid passports: ", num_correct)
