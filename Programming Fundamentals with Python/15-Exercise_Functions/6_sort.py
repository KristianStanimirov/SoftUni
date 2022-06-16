number_as_string = input().split()
numbers_as_digits = []

for current_number in number_as_string:
    numbers_as_digits.append(int(current_number))

result = list(sorted(numbers_as_digits))
print(result)
