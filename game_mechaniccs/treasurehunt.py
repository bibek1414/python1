import random
import csv

treasures=["sword "," coin","golden coin ","silver coin "," diamond"]
locations=["Lake", "Ruins"," Mountain","Forest","Temples"]
score=0
player_name=""

while True:
    user_input = input('''
1. Start Game
2. Load Game
3. Player Details
4. Score
5. Exit
Choose an option: ''')

    if user_input == "1":
        player_name = input("Enter your name: ")
        print(f"Welcome, {player_name}! The game will start soon.")
        for _ in range(3):
            location=random.choice(locations)
            treasure= random.choice(treasures)
            print(f"Exploring {location}...")
            print(f"You found a {treasure}!")
            score += 10
        print("Game Over! You've collected some treasures")
        with open("/home/bibek/Desktop/python1/game_mechaniccs/gamedata.csv", mode='a', newline="") as f:
                csv_writer = csv.writer(f)
                data=(player_name,score)
                csv_writer.writerow(data)

    elif user_input == "2":
        print("Game is loading... Please wait.")
        if player_name:
            print(f"Welcome back, {player_name}. Your current score is {score}.")
        else:
            print("No saved game Found .Please start a new game.")
        
    elif user_input == "3":
        if player_name:
            print(f"Player Name: {player_name} \n Score: {score}")
        else:
            print("No player data found. Please start the game first.")

    elif user_input == "4":
        print(f"Your current score is: {score}")
        
    elif user_input == "5":
        print("Exiting the game!")
        exit()
    
    else:
        print("Invalid option. Please choose a valid number.")
