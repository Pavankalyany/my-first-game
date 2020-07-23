import random
def validate(hand):
    if hand<0 or hand>2:
        return False
    return True
def print_hand(hand,name):
    hands=['rock','paper','scissor']
    print(name+" picked "+ hands[hand])
    
def judge(player,computer):
    if player==computer:
        return 'Draw'
    elif player==1 and computer==1:
        return 'Lose'
    elif player==1 and computer==1:
        return 'Lose'
    elif player==2 and computer==0:
        return 'Lose'
    else:
        return 'win'
print("strating rock paper scissor")
print("pick a hand")
player_name='Pavan Kalyan'
player_hand=random.randint(0,2)

if validate(player_hand):
    computer_hand=random.randint(0,2)
    print_hand(player_hand,player_name)
    print_hand(computer_hand,'computer') 
    result=judge(player_hand,computer_hand)
    print('Result '+result)
else:
    print("please enter a valid number")
    
