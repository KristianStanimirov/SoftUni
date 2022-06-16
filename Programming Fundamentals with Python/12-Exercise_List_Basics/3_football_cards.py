card = input()
cards_list = card.split(" ")
players_a = 11
players_b = 11
team_a = []
team_b = []

for i in cards_list:
    if "A" in i and i not in team_a:
        team_a.append(i)
        players_a -= 1
    elif "B" in i and i not in team_b:
        team_b.append(i)
        players_b -= 1
    if players_a < 7 or players_b < 7:
        break
print(f'Team A - {players_a}; Team B - {players_b}')
if players_a < 7 or players_b < 7:
    print("Game was terminated")
