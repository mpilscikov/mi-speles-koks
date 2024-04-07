from determine_winner import determine_winner
import tkinter as tk
from constants import ALLOWED_DIVISORS
from tree_generator import GameTreeGenerator, GameState
from tkinter import messagebox

def make_move(game_state, divisor):
    new_number = game_state.number // divisor
    new_points, new_bank = GameTreeGenerator.calculate_points_and_bank(new_number, game_state.points,
                                                                       game_state.bank)
    game_state = GameState(new_number, new_points, new_bank)
    return check_valid_moves(game_state)

def check_valid_moves(game_state):
    no_valid_moves = True
    for divisor in ALLOWED_DIVISORS:
        if game_state.number % divisor == 0:
            no_valid_moves = False
            break

    if no_valid_moves:
        winner = determine_winner(game_state)
        tk.messagebox.showinfo("Game Over", f"The winner is {winner}!")
        return None
    else:
        return game_state
