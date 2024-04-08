from constants import ALLOWED_DIVISORS

def player_move_logic(game_state):
    valid_moves_exist = False
    available_divisors = []
    for divisor in ALLOWED_DIVISORS:
        if game_state.number % divisor == 0:
            valid_moves_exist = True
            available_divisors.append(divisor)
    return valid_moves_exist, available_divisors
