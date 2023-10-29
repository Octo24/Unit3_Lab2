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