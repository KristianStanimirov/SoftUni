gifts_list = input().split()
COMMAND_out_of_stock = 'OutOfStock'
COMMAND_required = 'Required'
COMMAND_just_in_case = 'JustInCase'
command_list = []
command = input()

while command != 'No Money':
    if COMMAND_out_of_stock in command:
        command, gift = command.split()
        for current_gift in range(len(gifts_list)):
            if gifts_list[current_gift] == gift:
                gifts_list[current_gift] = 'None'
    elif COMMAND_required in command:
        command, gift, index = command.split()
        index = int(index)
        if 0 < index < len(gifts_list):
            gifts_list[index] = gift
    elif COMMAND_just_in_case in command:
        command, gift = command.split()
        gifts_list[-1] = gift
    command = input()
for i in range(len(gifts_list)):
    if 'None' in gifts_list:
        gifts_list.remove('None')

print(' '.join(gifts_list))
