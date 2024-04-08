def determine_winner(game_state, firstPlayer):
    if game_state.points % 2 == 1:
        total_points = game_state.points - game_state.bank
    else:
        total_points = game_state.points + game_state.bank

    if firstPlayer == "Player":
        if total_points % 2 == 0:
            return "AI"
        else:
            return "Player"
    else:
        if total_points % 2 == 0:
            return "Player"
        else:
            return "AI"
