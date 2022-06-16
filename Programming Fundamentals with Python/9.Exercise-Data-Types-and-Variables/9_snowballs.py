snowballs = int(input())
snowball_value = 0
max_weight = 0
time_needed = 0
quality = 0

for snowball in range(snowballs):

    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = int((current_weight / current_time) ** current_quality)

    if snowball_value < current_value:
        snowball_value = current_value
        max_weight = current_weight
        time_needed = current_time
        quality = current_quality

print(f"{max_weight} : {time_needed} = {snowball_value} ({quality})")
