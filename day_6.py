
def parse_file(filename):

    file = open(filename)

    groups = [[]]
    for line in file:
        if line == '\n':
            groups.append([])
            continue
        line = line[:-1] if line[-1] == '\n' else line
        groups[-1].append([])
        for letter in line:
            groups[-1][-1].append(letter)
    return groups


def intersection(list_1, list_2):
    return [value for value in list_1 if value in list_2]


groups = parse_file('resources/input_day_6.txt')

num_yes_answers = 0
for group in groups:
    yes_answers = []
    for person in group:
        yes_answers = yes_answers + person
    num_yes_answers = num_yes_answers + len(set(yes_answers))

print('\n*** Challenge 6 - Part 1: Number of yes answers is <%d>' % num_yes_answers)

num_yes_answers = 0
for group in groups:
    if len(group) == 1:
        num_yes_answers = num_yes_answers + len(group[0])
        continue
    set = group[0]
    for i in range(1, len(group)):
        set = intersection(set, group[i])
    num_yes_answers = num_yes_answers + len(set)

print('\n*** Challenge 6 - Part 2: Number of yes answers is <%d>' % num_yes_answers)


