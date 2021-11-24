def create_passport_list(filename):
    file = open(filename)
    passports = [{}]
    for line in file:
        if line == '\n':
            passports.append({})
            continue
        idx = 0
        while idx >= 0:
            if idx != 0:
                idx = idx + 1
            key = line[idx:line.find(':', idx)]
            idx = line.find(':', idx)
            if line.find(' ', idx) == -1 and line[-1] != '\n':  # special treatment for last line
                value = line[(idx + 1):]
            else:
                value = line[(idx + 1):line.find(' ', idx)]
            idx = line.find(' ', idx)

            passports[-1][key] = value
    return passports


def passport_valid(passport):
    necessary_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_keys = ['cid']
    for necessary_key in necessary_keys:
        if necessary_key not in passport:
            return False
    return True


def passport_valid_advanced(passport):
    if not (1920 <= int(passport['byr']) <= 2002):
        print('Remove %s due to wrong *byr*' % str(passport))
        return False
    if not (2010 <= int(passport['iyr']) <= 2020):
        print('Remove %s due to wrong *iyr*' % str(passport))
        return False
    if not (2020 <= int(passport['eyr']) <= 2030):
        print('Remove %s due to wrong *eyr*' % str(passport))
        return False
    if not ('cm' in passport['hgt'] or 'in' in passport['hgt']):
        print('Remove %s due to wrong *hgt*' % str(passport))
        return False
    if 'cm' in passport['hgt']:
        height = int(passport['hgt'][0: passport['hgt'].find('cm')])
        if not (150 <= height <= 193):
            print('Remove %s due to wrong *hgt*' % str(passport))
            return False
    elif 'in' in passport['hgt']:
        height = int(passport['hgt'][0: passport['hgt'].find('in')])
        if not (59 <= height <= 76):
            print('Remove %s due to wrong *hgt*' % str(passport))
            return False
    if passport['hcl'][0] != '#' or len(passport['hcl']) != 7:
        print('Remove %s due to wrong *hcl*' % str(passport))
        return False
    else:
        for char in passport['hcl'][1:]:
            if char not in ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('Remove %s due to wrong *hcl*' % str(passport))
                return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print('Remove %s due to wrong *ecl*' % str(passport))
        return False
    if len(passport['pid']) != 9:
        return False
    else:
        for char in passport['pid']:
            if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('Remove %s due to wrong *pid*' % str(passport))
                return False





    return True


num_passport_with_correct_keys = 0
num_valid = 0
passports = create_passport_list('resources/input_day_4.txt')
for passport in passports:
    if passport_valid(passport):
        num_passport_with_correct_keys = num_passport_with_correct_keys + 1
        if passport_valid_advanced(passport):
            num_valid = num_valid + 1

print('\n*** Result of challange part 1 is <%d> ***' % num_passport_with_correct_keys)
print('\n*** Result of challange part 2 is <%d> ***' % num_valid)
