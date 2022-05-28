command = input()
events = ('CODING', 'DOG', 'CAT', 'MOVIE')
number_of_coffees = 0
while command != 'END':
    for i in range(4):
        if command.upper() == events[i]:
            if command.isupper():
                number_of_coffees += 2
            else:
                number_of_coffees += 1
    command = input()

if number_of_coffees < 6:
    print(number_of_coffees)
else:
    print("You need extra sleep")
