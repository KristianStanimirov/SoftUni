cards_list = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(cards_list) // 2
    left_part = cards_list[0:middle_of_the_deck]
    right_part = cards_list[middle_of_the_deck::]
    for index_of_the_card in range(len(left_part)):
        final_deck.append(left_part[index_of_the_card])
        final_deck.append(right_part[index_of_the_card])
    cards_list = final_deck
print(cards_list)