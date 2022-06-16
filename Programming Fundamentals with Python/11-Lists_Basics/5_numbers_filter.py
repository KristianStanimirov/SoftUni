number = int(input())
numbers_list = []
filtered_list = []

for num in range(number):
    current_number = int(input())
    numbers_list.append(current_number)
command = input()

for i in range(len(numbers_list)):
    element = numbers_list[i]

    if command == 'even' and (element % 2 == 0 or element == 0):
        filtered_list.append(element)
    if command == 'odd' and element % 2 != 0:
        filtered_list.append(element)
    if command == 'negative' and element < 0:
        filtered_list.append(element)
    if command == 'positive' and element >= 0:
        filtered_list.append(element)
print(filtered_list)
