import random

# Game data
treasures = ["Gold Coin", "Silver Sword", "Mystic Orb", "Ancient Scroll"]
locations = ["Dark Cave", "Abandoned Castle", "Mysterious Forest", "Lost Temple"]
player_name = ""
score = 0

while True:
    user_input = input('''\n1. Start Game\n2. Load Game\n3. Player Details\n4. Score\n5. Exit\nChoose an option: ''')

    if user_input == "1":
        player_name = input("Enter your name: ")
        print(f"Welcome, {player_name}! The game will start soon.")
        for _ in range(3):
            location = random.choice(locations)
            treasure = random.choice(treasures)
            print(f"Exploring {location}...")
            print(f"You found a {treasure}!")
            score += 10
        print("Game Over! You've collected some treasures.")
        
    elif user_input == "2":
        print("Game is loading... Please wait.")
        if player_name:
            print(f"Welcome back, {player_name}. Your current score is {score}.")
        else:
            print("No saved game found. Please start a new game.")
        
    elif user_input == "3":
        if player_name:
            print(f"Player Name: {player_name}")
        else:
            print("No player data found. Please start the game first.")

    elif user_input == "4":
        print(f"Your current score is: {score}.")
        
    elif user_input == "5":
        print("Exiting the game!")
        break
    
    else:
        print("Invalid option. Please choose a valid number.")
