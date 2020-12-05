import re

passports = open("input.txt","r").read().split('\n\n')

codes = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

def is_valid(passport):
    for code in codes: 
        if code == 'cid':
            continue
        match = re.search(rf"{code}:(\S+)", passport) 
        if match == None:
            return False
        value = match.groups()[0]
        if value == None:
            return False
        if code == 'byr':
            if len(value) != 4 or int(value) < 1920 or int(value) > 2002:
                return False
        elif code == 'iyr':
            if len(value) != 4 or int(value) < 2010 or int(value) > 2020:
                return False
        elif code == 'eyr':
            if len(value) != 4 or int(value) < 2020 or int(value) > 2030:
                return False
        elif code == 'hgt':
            match = re.search(rf"^(\d+)(cm|in)$", value) 
            if match == None:
                return False
            value = match.groups()[0]
            unit = match.groups()[1]
            if value == None or unit == None:
                return False
            if unit == 'cm':
                if int(value) < 150 or int(value) > 193:
                    return False
            if unit == 'in':
                if int(value) < 59 or int(value) > 76:
                    return False
        elif code == 'hcl':
            match = re.search(r"^#[a-f\d]{6}$", value) 
            if match == None:
                return False
        elif code == 'ecl':
            match = re.search(r"^(amb|blu|brn|gry|grn|hzl|oth)$", value) 
            if match == None:
                return False
        elif code == 'pid':
            match = re.search(r"^\d{9}$", value) 
            if match == None:
                return False
    return True


valid_count = 0
for passport in passports:
    if is_valid(passport):
        valid_count += 1

print(valid_count)
