rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]

import random
choice=int(input("Choose any between rock, paper or scissors\n. Enter 0 for rock 1 for paper and 2 for scissors\n"))
print(game_images[choice])
choice_random=random.randint(0,2)
print("computer chooses")
print(game_images[choice_random])
if choice_random==0:
    print("rock")
elif choice_random==1:
    print("paper")
else:
    print("scissors")
if choice==0:
    if choice_random==0:
        print("Match drew")
    elif choice_random==1:
        print("you lose")
    else:
        print("you win")
if choice==1:
    if choice_random==0:
        print("you win")
    elif choice_random==1:
        print("match drew")
    else:
        print("you lose")
if choice==2:
    if choice_random==0:
        print("you lose")
    elif choice_random==1:
        print("you win")
    else:
        print("match drew")
