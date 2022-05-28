divisor = int(input())
boundary = int(input())
large_int = int()

for i in range(divisor, boundary + 1):
    if i % divisor == 0:
        large_int = i

print(large_int)
