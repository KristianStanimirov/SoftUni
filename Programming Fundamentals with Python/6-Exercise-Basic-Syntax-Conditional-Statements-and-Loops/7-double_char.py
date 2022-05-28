received_string = input()
new_string = ""

while not received_string == 'End':
    for i in range(len(received_string)):
        new_string += received_string[i] * 2
    if not received_string == "SoftUni":
        print(new_string)
    new_string = ""
    received_string = input()
