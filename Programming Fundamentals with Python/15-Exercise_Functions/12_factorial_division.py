# def factorial_function(number):
#     for factorial in range(1, number):
#         number *= factorial
#     return number

import math

first_number = int(input())
second_number = int(input())

fact_first_number = math.factorial(first_number)
fact_second_number = math.factorial(second_number)

result = fact_first_number / fact_second_number
print(f"{result:.2f}")
