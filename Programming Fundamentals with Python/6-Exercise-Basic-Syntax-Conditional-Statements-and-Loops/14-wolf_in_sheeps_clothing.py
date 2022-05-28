queue = input()
queue_list = queue.rsplit(', ')
queue_list.reverse()
wolf_number = queue_list.index('wolf') + 1
sheep_to_be_eaten = wolf_number - 1
if wolf_number == 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_to_be_eaten}! You are about to be eaten by a wolf!")

