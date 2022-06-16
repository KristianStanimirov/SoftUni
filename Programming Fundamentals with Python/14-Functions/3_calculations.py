operator = input()
number_a = int(input())
number_b = int(input())


def calculation_func(num_a: int, num_b: int, operation: str):
    result = None
    if operation == "multiply":
        result = num_a * num_b
    elif operation == "divide":
        result = num_a // num_b
    elif operation == "add":
        result = num_a + num_b
    elif operation == "subtract":
        result = num_a - num_b
    return result


print(calculation_func(number_a, number_b, operator))
