def determine_winner(game_state):
    if game_state.points % 2 == 1:
        total_points = game_state.points - game_state.bank
    else:
        total_points = game_state.points + game_state.bank

    if total_points % 2 == 0:
        return "AI"
    else:
        return "Player"
