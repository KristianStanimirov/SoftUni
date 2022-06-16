list_numbers = input().split()
rounded_list = []


def round_func(num: float):
    result = round(num)
    return result


for number in list_numbers:
    round_num = round_func(float(number))
    rounded_list.append(round_num)

print(rounded_list)
