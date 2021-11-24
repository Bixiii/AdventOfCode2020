
def parse_boarding_pass(boarding_pass):
    assert(len(boarding_pass) == 10)
    return boarding_pass[:7], boarding_pass[7:]


def decode_row(row):
    min = 0
    max = 127
    for letter in row:
        range = max - min
        if letter == 'F':
            max = min + range//2
        else:  # letter == 'F'
            min = min + range//2 + 1

    assert(min == max)
    return min


def decode_column(column):
    min = 0
    max = 7
    for letter in column:
        range = max - min
        if letter == 'L':
            max = min + range//2
        else:  # letter == 'R'
            min = min + range//2 + 1

    assert(min == max)
    return min


def calculate_ticket_id(row, column):
    return decode_row(row) * 8 + decode_column(column)


file = open('resources/input_day_5.txt')
boarding_pass_list = []
for line in file:
    if line[-1] == '\n':
        boarding_pass_list.append(line[:-1])
    else:
        boarding_pass_list.append(line)


ids = []
for boarding_pass in boarding_pass_list:
    ids.append(calculate_ticket_id(*parse_boarding_pass(boarding_pass)))

print('\n*** Challenge 5 - Part 1: max_id is <%d>' % (max(ids)))

for id in range(min(ids), max(ids), 1):
    if id not in ids:
        print('\n*** Challenge 5 - Part 2: missing id <%d>' % id)
