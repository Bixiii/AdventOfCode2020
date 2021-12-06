
input_file = open('resources/input_day_9.txt')

number_sequence = []
for line in input_file:
    number_sequence.append(int(line[:-1]))


window_size = 25
position = 25

valid = False
first_error_number = -1
while position < len(number_sequence):
    for a in range(position-window_size, position):
        valid = False
        for b in range(position-window_size, position):
            if a == b:
                continue
            if (number_sequence[a] + number_sequence[b]) == number_sequence[position]:
                valid = True
                break
        if valid:
            break
    if not valid:
        first_error_number = number_sequence[position]
        break
    position = position + 1

print('\n*** Challenge 9 - Part 1: ', first_error_number)

start = 0
end = 1
sum = number_sequence[0]

while sum != first_error_number:
    sum = sum - number_sequence[start]
    while sum < first_error_number:
        sum = sum + number_sequence[end]
        end = end + 1
    if sum == first_error_number:
        print('\n*** Challenge 9 - Part 2: <%d>' % (min(number_sequence[start+1:end-1]) + max(number_sequence[start+1:end-1])))
    start = start + 1
