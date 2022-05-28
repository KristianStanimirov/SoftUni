received_name = input()

while received_name != 'Welcome!':
    if received_name == 'Voldemort':
        print('You must not speak of that name!')
        break
    if len(received_name) < 5:
        print(f"{received_name} goes to Gryffindor.")
    elif len(received_name) == 5:
        print(f"{received_name} goes to Slytherin.")
    elif len(received_name) == 6:
        print(f"{received_name} goes to Ravenclaw.")
    else:
        print(f"{received_name} goes to Hufflepuff.")
    received_name = input()

if received_name == 'Welcome!':
    print("Welcome to Hogwarts.")
