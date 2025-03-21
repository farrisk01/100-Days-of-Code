import random

"""
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

############ Computer generated choose
_randocomputer = random.randint(1, 3)
_playchoose = input('Choose 1 for rock, 2 for paper, 3 for scissors:\n')

if _playchoose == '1':
    print('You choose:\n', rock)
elif _playchoose == '2':
    print('You choose:\n', paper)
else:
    print('You choose:\n', scissors)

if _randocomputer == 1:
    print('Computer chose:\n', rock)
elif _randocomputer == '2':
    print('Computer chose:\n', paper)
else:
    print('Computer chose:\n', scissors)

if _playchoose == '1':
    if _randocomputer == 1:
        print('Tie')
    elif _randocomputer == 2:
        print('You win!')
    else:
        print('Computer wins!')
elif _playchoose == '2':
    if _randocomputer == 1:
        print('Computer wins!')
    elif _randocomputer == 2:
        print('Tie')
    else:
        print("You win!")
elif _playchoose == '3':
    if _randocomputer == 1:
        print('You win!')
    elif _randocomputer == 2:
        print('Computer wins!')
    else:
        print("Tie")

else:
    print('Invalid choice!')

"""
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
"""