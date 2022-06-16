list_of_integer = input().split()
count_of_numbers_to_remove = int(input())
number_to_int = []

# list to integer
for element in list_of_integer:
    number_to_int.append(int(element))

# removing of the min number
for index in range(count_of_numbers_to_remove):
    number_to_int.remove(min(number_to_int))

# create the final string for printing
final_numbers = ''
for i in range(len(number_to_int)):
    if i == len(number_to_int) - 1:
        final_numbers += str(number_to_int[i])
    else:
        final_numbers += str(number_to_int[i]) + ", "
print(final_numbers)
