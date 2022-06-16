level_of_fire = input().split("#")
amount_of_water = int(input())
effort = 0
total_fire = 0


def fire_type_func(type_fire: str, fire_value: int):
    if type_fire == 'High' and 81 <= fire_value <= 125:
        is_valid = True
    elif type_fire == 'Medium' and 51 <= fire_value <= 80:
        is_valid = True
    elif type_fire == 'Low' and 1 <= fire_value <= 50:
        is_valid = True
    else:
        is_valid = False
    return is_valid


print("Cells:")
for cell in level_of_fire:
    type_of_fire, value_cells = cell.split(" = ")
    value_cells = int(value_cells)
    if amount_of_water >= value_cells:
        if fire_type_func(type_of_fire, value_cells):
            amount_of_water -= value_cells
            effort += value_cells * 0.25
            total_fire += value_cells
            print(f' - {value_cells}')

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
