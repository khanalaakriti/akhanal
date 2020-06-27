import random

my_dict= {}

def dice_game():
    players= int(input('How many players are there?: '))
    players = players + 1
    for i in range(1, players):
        player_name = input('What is your name?: ')
        roll_die= random.randint(1,6)
        print('Dice rolled for', player_name, ':', roll_die)
        my_dict[player_name] = roll_die

dice_game()

print('=========================================================================')

max_score = 0
#print('Start with maximum score of:', max_score)
for key in my_dict:
    score = my_dict[key]
    #print('Question -> Is', score, 'greater than', max_score,'?')
    if(score > max_score):
        max_score = score
    #    #print('Answer -> Yes, so change the maximum score to:', max_score)
    #else:
    #    print('Answer -> No, so keep maximum score:', max_score)

#print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

print('The maximum score is:', max_score)       
for player, player_score in my_dict.items():
    if player_score == max_score:
        print('Player', player, 'has the maximum score')
