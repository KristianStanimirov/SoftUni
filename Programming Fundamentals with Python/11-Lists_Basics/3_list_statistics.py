number = int(input())
positive_list = []
negative_list = []

for num in range(number):
    current_number = int(input())
    if current_number >= 0:
        positive_list.append(current_number)
    else:
        negative_list.append(current_number)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}\nSum of negatives: {sum(negative_list)}")