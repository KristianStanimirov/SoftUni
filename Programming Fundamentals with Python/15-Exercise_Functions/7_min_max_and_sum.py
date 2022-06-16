numbers_as_string = input().split()
numbers_as_digits = []

for current_number in numbers_as_string:
    numbers_as_digits.append(int(current_number))

min_number = min(numbers_as_digits)
max_number = max(numbers_as_digits)
sum_numbers = sum(numbers_as_digits)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")
