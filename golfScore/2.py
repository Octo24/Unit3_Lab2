while True:
    players = int(input("How many players (max 4): "))
    
    if 1 <= players <= 4:
        player_names = []
        player_scores = {}
        
        # add player names to list
        for i in range(1, players + 1):
            name = input(f"Input Player {i} Name: ")
            player_names.append(name)
        print("Player name(s): ", player_names)

        # player names & scores to dictionary
        for name in player_names:
            score = int(input(f"Enter {name}'s score: "))
            player_scores[name] = score
        print(f"Player score(s): {player_scores}")

    else:
        print("Invalid input, please enter a valid number of players (1 to 4): ")
        continue 

    with open("golfScore/outputs.txt", "w") as output_counts:
        output_counts.write(f"GOLF SCORES: {player_scores}")