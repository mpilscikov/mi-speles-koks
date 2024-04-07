import tkinter as tk
from tree_generator import GameState
from player_move import player_move_logic
import random
from constants import ALLOWED_DIVISORS
from ai_move import ai_move
from make_move import make_move
from make_move import check_valid_moves

class GameUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Game")
        self.game_state = None
        self.algorithm = None
        self.player_first = None
        self.master.geometry("400x600")
        self.generate_selection_screen()

    def generate_selection_screen(self):
        selection_frame = tk.Frame(self.master)
        selection_frame.pack(expand=True)

        tk.Label(selection_frame, text="Choose who moves first:").pack()
        tk.Button(selection_frame, text="Player",
                  command=lambda: self.set_first_move("Player"), width=15, height=2).pack()
        tk.Button(selection_frame, text="AI",
                  command=lambda: self.set_first_move("AI"), width=15, height=2).pack()

    def set_first_move(self, player_first):
        self.player_first = player_first
        self.generate_algorithm_selection()

    def generate_algorithm_selection(self):
        selection_frame = tk.Frame(self.master)
        selection_frame.pack(expand=True)

        tk.Label(selection_frame, text="Choose an algorithm:").pack()
        tk.Button(selection_frame, text="Minimax",
                  command=self.set_minimax_algorithm, width=15, height=2).pack()
        tk.Button(selection_frame, text="Alpha-Beta",
                  command=self.set_alpha_beta_algorithm, width=15, height=2).pack()

    def set_minimax_algorithm(self):
        self.algorithm = "minimax"
        self.generate_number_selection()

    def set_alpha_beta_algorithm(self):
        self.algorithm = "alpha_beta"
        self.generate_number_selection()

    def generate_number_selection(self):
        number_frame = tk.Frame(self.master)
        number_frame.pack(expand=True)

        tk.Label(number_frame, text="Choose a number to start the game:").pack()

        for _ in range(5):
            number = random.randint(30000, 50000)
            button = tk.Button(number_frame, text=str(number),
                               command=lambda num=number: self.start_game(num), width=15, height=2)
            button.pack(anchor="center", pady=5)

    def start_game(self, number):
        self.game_state = GameState(number, 0, 0)
        self.clear_selection_screen()
        self.create_labels()

        if self.player_first == "Player":
            self.player_move()
        else:
            self.ai_move()

    def clear_selection_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def create_labels(self):
        labels_frame = tk.Frame(self.master)
        labels_frame.pack(expand=True)

        self.number_label = tk.Label(labels_frame, text=f"Current Number: {self.game_state.number}")
        self.number_label.pack(anchor="center", pady=5)

        self.points_label = tk.Label(labels_frame, text=f"Points: {self.game_state.points}")
        self.points_label.pack(anchor="center", pady=5)

        self.bank_label = tk.Label(labels_frame, text=f"Bank: {self.game_state.bank}")
        self.bank_label.pack(anchor="center", pady=5)

    def player_move(self):
        self.clear_move_buttons()
        valid_moves_exist, available_divisors = player_move_logic(self.game_state)
        for divisor in ALLOWED_DIVISORS:
            if divisor in available_divisors:
                button = tk.Button(self.master, text=f"Divide by {divisor}",
                                   command=lambda num=divisor: self.make_move(num), width=15, height=2)
                button.pack(anchor="center", pady=5)
            else:
                button = tk.Button(self.master, text=f"Can't divide by {divisor}",
                                   command=lambda: None, width=15, height=2, state="disabled")
                button.pack(anchor="center", pady=5)

    def clear_move_buttons(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button):
                widget.pack_forget()

    def make_move(self, divisor):
        self.game_state = make_move(self.game_state, divisor)
        self.update_labels()
        if self.game_state is not None:
            self.player_move()
            self.ai_move()
            self.update_labels()

    def ai_move(self):
        self.game_state = ai_move(self.game_state, self.algorithm,self.player_first)
        if self.game_state is not None:
            self.player_move()

    def update_labels(self):
        if self.game_state is None:
            return
        self.number_label.config(text=f"Current Number: {self.game_state.number}")
        self.points_label.config(text=f"Points: {self.game_state.points}")
        self.bank_label.config(text=f"Bank: {self.game_state.bank}")
        check_valid_moves(self.game_state)
