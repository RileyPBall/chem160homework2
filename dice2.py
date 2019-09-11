from random import choices
ntrials = 10000
player1wins = 0
player2dice = 2
player1dice = 3
for i in range(ntrials):
    dice2=choices(range(1,7), k=player2dice)
    total2 = dice2[0]+dice2[1]
    if dice2[0]==dice2[1]:
        continue
    dice1=choices(range(1,7), k=player1dice)
    dice1.sort(reverse=True)
    total1= dice1[0]+dice1[1]
    if dice1[0]**2 + dice1[1]**2 == 8:
        continue
    if dice1[0]**2 + dice1[2]**2 == 8:
        continue
    if dice1[1]**2 + dice1[2]**2 == 8:
        continue
    if total1 > total2:
        player1wins+=1
print("ratio of player 1 wins=", player1wins/ntrials)