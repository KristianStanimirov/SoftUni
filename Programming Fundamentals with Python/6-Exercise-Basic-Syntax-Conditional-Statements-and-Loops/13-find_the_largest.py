number = int(input())
largest_number = ''
max_digit = 0

list_number = list(str(number))

for digit in range(len(str(number))):
    max_digit = max(list_number)
    largest_number += str(max_digit)
    list_number.remove(max_digit)
print(largest_number)
