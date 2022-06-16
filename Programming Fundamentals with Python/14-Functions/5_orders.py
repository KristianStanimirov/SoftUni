def order_func(product: str, quantity: int):
    prices = None
    if product == "coffee":
        prices = 1.50
    elif product == "coke":
        prices = 1.40
    elif product == "water":
        prices = 1.00
    elif product == "snacks":
        prices = 2.00

    result = prices * quantity
    return f'{result:.2f}'


products = input()
number_quantity = int(input())

print(order_func(products, number_quantity))
