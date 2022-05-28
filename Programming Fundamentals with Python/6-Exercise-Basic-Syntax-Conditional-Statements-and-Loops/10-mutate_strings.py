first_string = input()
second_string = input()
last_string = first_string

# slice(start, end, step)

for symbol_index in range(len(second_string)):
    left_part = second_string[:symbol_index + 1]  # [0:symbol+1:1]
    right_part = first_string[symbol_index + 1:]  # [0:len(first_string):1
    current_string = left_part + right_part

    if last_string == current_string:
        continue
    print(current_string)
    last_string = current_string

