def is_palindrome(number):
    if str(number)[::-1] == str(number):
        result = True
    else:
        result = False
    return result


numbers_as_string = input().split(", ")
numbers_as_digits = []

for current_number in numbers_as_string:
    numbers_as_digits.append(int(current_number))

for current_digits in numbers_as_digits:
    print(is_palindrome(current_digits))
