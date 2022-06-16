integer_string = input().split(", ")
count_of_beggars = int(input())
final_list = []
counter_of_index = 0
sums_list_of_digits = []

for element in integer_string:
    sums_list_of_digits.append(int(element))

while counter_of_index < count_of_beggars:
    sum_of_current_beggar = 0
    for element in range(counter_of_index,len(sums_list_of_digits),count_of_beggars):
        sum_of_current_beggar += sums_list_of_digits[element]
    counter_of_index += 1
    final_list.append(sum_of_current_beggar)
print(final_list)