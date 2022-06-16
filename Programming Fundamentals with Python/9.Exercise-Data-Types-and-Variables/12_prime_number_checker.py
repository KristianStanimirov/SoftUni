number = int(input())
prime_number = False

for i in range(2, number // 2):
    if number % i == 0:
        prime_number = False
        break
    else:
        prime_number = True

print(prime_number)