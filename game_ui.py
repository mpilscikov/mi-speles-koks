import tkinter as tk
from tkinter import messagebox
from tree_generator import GameState, GameTreeGenerator
from constants import ALLOWED_DIVISORS
import random


class GameUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Game")
        self.game_state = None
        self.algorithm = None
        self.master.geometry("400x600")
        self.generate_selection_screen()

    def generate_selection_screen(self):
        selection_frame = tk.Frame(self.master)
        selection_frame.pack(expand=True)
        tk.Label(selection_frame, text="Choose an algorithm: ").pack()
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
        for divisor in ALLOWED_DIVISORS:
            button = tk.Button(self.master, text=f"Divide by {divisor}",
                               command=lambda num=divisor: self.make_move(num), width=15, height=2)
            button.pack(anchor="center", pady=5)

    def clear_selection_screen(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()

    def create_labels(self):
        labels_frame = tk.Frame(self.master)
        labels_frame.pack(expand=True)

        # Create labels
        self.number_label = tk.Label(labels_frame, text=f"Current Number: {self.game_state.number}")
        self.number_label.pack(anchor="center", pady=5)

        self.points_label = tk.Label(labels_frame, text=f"Points: {self.game_state.points}")
        self.points_label.pack(anchor="center", pady=5)

        self.bank_label = tk.Label(labels_frame, text=f"Bank: {self.game_state.bank}")
        self.bank_label.pack(anchor="center", pady=5)

    def make_move(self, divisor):
        if self.game_state.number % divisor == 0:
            new_number = self.game_state.number // divisor
            new_points, new_bank = GameTreeGenerator.calculate_points_and_bank(
                new_number, self.game_state.points, self.game_state.bank)
            self.game_state = GameState(new_number, new_points, new_bank)
            self.update_labels()

            divisible = any(self.game_state.number %
                            d == 0 for d in ALLOWED_DIVISORS)
            if not divisible:
                if self.game_state.points % 2 == 1:
                    new_points = self.game_state.points - self.game_state.bank
                else:
                    new_points = self.game_state.points + self.game_state.bank

                if new_points % 2 == 1:
                    winner = "Player 1"
                else:
                    winner = "Player 2"

                tk.messagebox.showinfo("Game Over", f"The winner is {winner}!")

    def update_labels(self):
        self.number_label.config(
            text=f"Current Number: {self.game_state.number}")
        self.points_label.config(text=f"Points: {self.game_state.points}")
        self.bank_label.config(text=f"Bank: {self.game_state.bank}")
