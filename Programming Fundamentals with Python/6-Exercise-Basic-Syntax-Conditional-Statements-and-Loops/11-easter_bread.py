budget = float(input())
price_flour = float(input())
price_pack_eggs = 0.75 * price_flour
price_liter_milk = price_flour + (price_flour * 0.25)
number_of_loaves = 0
colored_eggs = 0
lost_eggs = 0
price_of_loaf = price_pack_eggs + price_flour + (price_liter_milk / 4)


while budget >= price_of_loaf:
    number_of_loaves += 1
    budget -= price_of_loaf
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        lost_eggs += number_of_loaves - 2


colored_eggs -= lost_eggs

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
