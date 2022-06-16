string = input()
counter = int(input())

# repeating_string = lambda a, b: a * b


def repeat_func(strings: str, number: int):
    result = strings * number

    return result


print(repeat_func(string, counter))
