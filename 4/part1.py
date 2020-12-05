import re

passports = open("input.txt","r").read().split('\n\n')

codes = [
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',
    #'cid',
]



def is_valid(passport):
    for code in codes: 
        regex = rf"{code}:\S+"
        match = re.search(regex, passport) 
        if match == None:
            return False
    return True


valid_count = 0
for passport in passports:
    if is_valid(passport):
        valid_count += 1

print(valid_count)
