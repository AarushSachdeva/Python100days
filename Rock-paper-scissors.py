import random
Won=Lost=Draw=0
possible_choices=["rock","paper","scissors"]
while(True):
    player=input("Enter a choice (rock,paper,scissors): ")
    system_action=random.choice(possible_choices)
    if player==system_action:
     print(f"Draw as your choice is {player} and computer choice is {system_action}")
     Draw=Draw+1
    elif player=="rock" and system_action=="scissors":
     print(f"You Win this game!!.Your choice was {player} and Computer choice was {system_action}")
     Won=Won+1
    elif player=="paper" and system_action=="rock":
     print(f"You Win this game!!.Your choice was {player} and Computer choice was {system_action}")
     Won=Won+1
    elif player=="scissors" and system_action=="paper":
     print(f"You Win this game!!.Your choice was {player} and Computer choice was {system_action}")
     Won=Won+1
    else:
     print(f"You lose this game.Your choice was {player} and Computer choice was {system_action}")
     Lose=Lose+1
    print(f"Current score of You V/S Computer is Won:{Won} Lost:{Lost} Draw:{Draw}")
    play_again=input("Play again? (yes/no):")
    if play_again=="no":
        break
