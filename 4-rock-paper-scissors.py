import random
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
choice=int(input("Enter 0 for Rock, 1 for Paper or 2 for Scissors:"))
print("YOU: ")
if choice==0:
    print(rock)
elif choice==1:
    print(paper)
elif choice==2:
    print(scissors)
comp=int(random.randint(0,2))
print(f"Computer chooses {comp}")
print("COMPUTER: ")
if comp==0:
    print(rock)
elif comp==1:
    print(paper)
else:
    print(scissors)
if choice==0 & comp==1:
    print("Computer Wins!")
elif choice == 1 & comp == 2:
    print("Computer Wins!")
elif choice == 2 & comp == 0:
    print("Computer Wins!")
elif choice == 0 & comp == 2:
    print("You Win!")
elif choice == 1 & comp == 0:
    print("You Win!")
elif choice==2 & comp==1:
    print("You Win!")
elif comp==choice:
    print("TIE!!!")
