from alpha_beta import AlphaBeta
from tree_generator import GameState, GameTreeGenerator
from constants import ALLOWED_DIVISORS
from minimax import Minimax


def ai_move(game_state, algorithm, player_first):
    if algorithm == "minimax":
        best_value = float("-inf")
        best_move = None

        for divisor in ALLOWED_DIVISORS:
            if game_state.number % divisor == 0:
                new_number = game_state.number // divisor
                new_points, new_bank = GameTreeGenerator.calculate_points_and_bank(new_number,
                                                                                   game_state.points,
                                                                                   game_state.bank)
                new_state = GameState(new_number, new_points, new_bank)
                value = Minimax.minimax(GameTreeGenerator.generate_tree(new_state), depth=20,
                                        maximizing_player=False, firstPlayer=player_first)
                if value > best_value:
                    best_value = value
                    best_move = divisor

        if best_move is not None:
            new_number = game_state.number // best_move
            new_points, new_bank = GameTreeGenerator.calculate_points_and_bank(new_number,
                                                                               game_state.points,
                                                                               game_state.bank)
            game_state = GameState(new_number, new_points, new_bank)
            # for debugging
            print(f"AI chose to divide by {best_move}, {new_number}")
            return game_state

    elif algorithm == "alpha_beta":
        best_value = float("-inf")
        best_move = None

        for divisor in ALLOWED_DIVISORS:
            if game_state.number % divisor == 0:
                new_number = game_state.number // divisor
                new_points, new_bank = GameTreeGenerator.calculate_points_and_bank(new_number,
                                                                                   game_state.points,
                                                                                   game_state.bank)
                new_state = GameState(new_number, new_points, new_bank)
                value = AlphaBeta.alpha_beta(GameTreeGenerator.generate_tree(new_state), depth=20,
                                             alpha=float("-inf"), beta=float("inf"), maximizing_player=False,
                                             firstPlayer=player_first)
                if value > best_value:
                    best_value = value
                    best_move = divisor

        if best_move is not None:
            new_number = game_state.number // best_move
            new_points, new_bank = GameTreeGenerator.calculate_points_and_bank(new_number,
                                                                               game_state.points,
                                                                               game_state.bank)
            game_state = GameState(new_number, new_points, new_bank)

            # for debugging
            print(f"AI chose to divide by {best_move}, {new_number}")
            return game_state
