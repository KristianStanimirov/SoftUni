a: float = float(input())

if 0 == a:
    print("zero")
elif 0 < a:
    if abs(a) < 1:
        print("small positive")
    elif abs(a) > 1000000:
        print("large positive")
    else:
        print("positive")
elif 0 > a:
    if abs(a) < 1:
        print("small negative")
    elif abs(a) > 1000000:
        print("large negative")
    else:
        print("negative")
