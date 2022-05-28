number_of_orders = int(input())
total_price = 0

for i in range(number_of_orders):

    price_per_capsule = float(input())
    days = int(input())
    capsules_needs_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if 1 > capsules_needs_per_day or capsules_needs_per_day > 2000:
        continue

    order_price = price_per_capsule * days * capsules_needs_per_day
    total_price += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total_price:.2f}")
