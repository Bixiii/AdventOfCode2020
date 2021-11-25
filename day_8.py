input_file = open('resources/input_day_8.txt')

program = []
for command in input_file:
    program.append({'command': command, 'visited': False})


def extract_number(number):
    sign = number[4]
    if sign == '+':
        return int(number[5:-1])
    elif sign == '-':
        return - int(number[5:-1])


def run_program():
    position = 0
    accumulator = 0
    last_position = len(program) - 1
    terminated = False

    while True:

        if position == last_position:
            terminated = True
            break

        if program[position]['visited'] is True:
            break

        program[position]['visited'] = True

        current_command = program[position]['command']
        if 'acc' in current_command:
            accumulator = accumulator + extract_number(current_command)
            position = position + 1
        if 'jmp' in current_command:
            position = position + extract_number(current_command)
        if 'nop' in current_command:
            position = position + 1

    return accumulator, terminated


def reset_program():
    for i, _ in enumerate(program):
        program[i]['visited'] = False


accumulator, _ = run_program()
print('\n*** Challenge 8 - Part 1: Accumulator is %d\n\n' % (accumulator))

# Brute force, because why would I bother thinking about something clever

for position, command in enumerate(program):
    reset_program()

    if 'jmp' in command['command']:
        program[position]['command'] = program[position]['command'].replace('jmp', 'nop')
        accumulator, terminated = run_program()
        if terminated:
            print('We found it! Replace jmp on line <%d>' % (position + 1))
            break
        else:
            program[position]['command'] = program[position]['command'].replace('nop', 'jmp')

    if 'nop' in command['command']:
        program[position]['command'] = program[position]['command'].replace('nop', 'jmp')
        accumulator, terminated = run_program()
        if terminated:
            print('We found it! Replace nop on line <%d>' % (position + 1))
            break
        else:
            program[position]['command'] = program[position]['command'].replace('jmp', 'nop')

reset_program()
accumulator, _ = run_program()
print('\n*** Challenge 8 - Part 2: Accumulator in fixed program is %d\n\n' % (accumulator))
