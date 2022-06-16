def loading_bar(num):
    if num < 100:
        return "Still loading..."
    else:
        return "[%%%%%%%%%%]"


def percent_message(num):
    if num < 100:
        return f"{num}% [{percent * int(num / 10)}{dot * (10 - int(num / 10))}]"

    else:
        return "100% Complete!"


number = int(input())
percent = "%"
dot = "."

print(percent_message(number))
print(loading_bar(number))
