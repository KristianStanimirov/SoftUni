budget = int(input())
command = input()

while command != "End":
    prices = int(command)
    budget -= prices
    if budget >= 0:
        command = input()
        continue
    print("You went in overdraft!")
    break
else:
    print('You bought everything needed.')
