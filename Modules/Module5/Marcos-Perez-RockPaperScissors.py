import random
from typing import ItemsView
print("Welcome to Rock, Paper, Scissors Showdown!")
RockPaperScissors = ["rock", "paper", "scissor"]

my_choice = input("You're the worst player I've ever seen. You'll never beat me. Choose: rock, paper, scissors \n")

computer_choice = random.choice(RockPaperScissors)
print(f"Computer selected: {computer_choice}")
print(f"Player selected: {my_choice}")

if(my_choice == computer_choice):
    print("We're tied 😤")

elif(my_choice == "rock" and computer_choice == "scissors"):
    print("I am the winner! Its obvious, I am the best. 😎")

elif(my_choice == "rock" and computer_choice == "paper"):
    print("No, YOU'RE the worst 😆")

elif(my_choice == "paper" and computer_choice == "scissors"):
    print("If only you were better... 🙄")

elif(my_choice == "paper" and computer_choice == "rock"):
    print("Did you actually think you were going to win? 🤭")

elif(my_choice == "scissors" and computer_choice == "rock"):
    print("Let me take that victory off your hands.")

elif(my_choice == "scissors" and computer_choice == "paper"):
    print("That was easy 😴. Where's the money?! 🤑🤑🤑🤑🤑")

else:
    print("Something is not right.")