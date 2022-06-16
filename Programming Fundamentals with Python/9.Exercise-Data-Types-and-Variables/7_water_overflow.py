capacity = 255
lines = int(input())
sum_liters = 0
for i in range(lines):
    liters = int(input())
    if liters > capacity:
        print('Insufficient capacity!')
        break
    sum_liters += liters

    if sum_liters > capacity:
        print('Insufficient capacity!')
        sum_liters -= liters
print(sum_liters)
