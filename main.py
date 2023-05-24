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

#Write your code below this line 👇
import random
options_list=[scissors,rock,paper]
user_choice = input("Choose:- Rock,Paper or Scissors Type in terms of R,P and S respectively - ").lower()
computer_choice = random.choice(options_list)
if user_choice == "r" and computer_choice == rock:
    print(rock)
    print("Computer chose:-")
    print(computer_choice)
    print("It's a draw")
elif user_choice == "r" and computer_choice == paper:
    print(rock)
    print("Computer Chose:- ")
    print(computer_choice)
    print("Sorry But You Lost")
elif user_choice == "r" and computer_choice == scissors:
    print(rock)
    print("Computer Chose:- ")
    print(computer_choice)
    print("Congrats You Won")
if user_choice == "s" and computer_choice == scissors:
    print(scissors)
    print("Computer chose:-")
    print(computer_choice)
    print("It's a draw")
elif user_choice == "s" and computer_choice == rock:
    print(scissors)
    print("Computer Chose:- ")
    print(computer_choice)
    print("Sorry But You Lost")
elif user_choice == "s" and computer_choice == paper:
    print(scissors)
    print("Computer Chose:- ")
    print(computer_choice)
    print("Congrats You Won")
if user_choice == "p" and computer_choice == paper:
    print(paper)
    print("Computer chose:-")
    print(computer_choice)
    print("It's a draw")
elif user_choice == "p" and computer_choice == scissors:
    print(paper)
    print("Computer Chose:- ")
    print(computer_choice)
    print("Sorry But You Lost")
elif user_choice == "p" and computer_choice == rock:
    print(paper)
    print("Computer Chose:- ")
    print(computer_choice)
    print("Congrats You Won")