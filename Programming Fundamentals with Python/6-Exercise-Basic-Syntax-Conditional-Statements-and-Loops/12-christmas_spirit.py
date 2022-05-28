quantity_of_decoration = int(input())
days_left = int(input())

ornament_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

budget = 0
total_spirit = 0


for i in range(1, days_left + 1):
    if i % 11 == 0:
        quantity_of_decoration += 2
    if i % 2 == 0:
        budget += ornament_price * quantity_of_decoration
        total_spirit += 5
    if i % 3 == 0:
        budget += (tree_skirt_price + tree_garland_price) * quantity_of_decoration
        total_spirit += 13
    if i % 5 == 0:
        budget += tree_lights_price * quantity_of_decoration
        total_spirit += 17
    if i % 3 == 0 and i % 5 == 0:
        total_spirit += 30
    if i % 10 == 0:
        total_spirit -= 20
        budget += tree_skirt_price + tree_garland_price + tree_lights_price

if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
