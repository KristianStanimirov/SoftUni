list_of_string = input().split()
list_of_numbers = []

for num in list_of_string:
    number = float(num)
    list_of_numbers.append(number)

list_of_abs_num = []

for num in list_of_numbers:
    number = abs(num)
    list_of_abs_num.append(number)

print(list_of_abs_num)

