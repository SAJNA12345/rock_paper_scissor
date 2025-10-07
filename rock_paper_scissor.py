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
print("Welcome to the Rock Paper Scissors Game!")
print("Type 0 for rock,1 for paper and 2 for scissors")
no=int(input())
if(no>2):
    print("Please enter a number between 1 and 2")
else:
    print("You chose:")
    print(no)
    l1=[rock,paper,scissors]

    random_no=random.choice(l1)
    print("Computer chose:")
    print(random_no)
    if(no==0 and random_no==rock):
        print("Its a draw")
    elif no==1 and random_no==paper:
        print("Its a draw")
    elif no==2 and random_no==scissors:
        print("Its a draw")
    elif no==0 and random_no==paper:
        print("You lose")
    elif no==1 and random_no==rock:
        print("You win")
    elif no==1 and random_no==scissors:
        print("You lose")
    elif no==2 and random_no==paper:
        print("You win")


