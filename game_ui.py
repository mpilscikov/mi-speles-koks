import tkinter as tk
from tree_generator import GameState
from constants import ALLOWED_DIVISORS
import random

class GameUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Game")
        self.game_state = None
        self.generate_number_selection()

    def generate_number_selection(self):
        tk.Label(self.master, text="Choose a number to start the game:").pack()
        for _ in range(5):
            number = random.randint(30000, 50000)
            tk.Button(self.master, text=str(number), command=lambda num=number: self.start_game(num)).pack()

    def start_game(self, number):
        self.game_state = GameState(number, 0, 0)
        self.clear_number_selection()
        self.create_labels()
        for divisor in ALLOWED_DIVISORS:
            tk.Button(self.master, text=f"Divide by {divisor}", command=lambda num=divisor: self.make_move(num)).pack()

    def clear_number_selection(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()

    def create_labels(self):
        self.number_label = tk.Label(self.master, text=f"Current Number: {self.game_state.number}")
        self.number_label.pack()
        self.points_label = tk.Label(self.master, text=f"Points: {self.game_state.points}")
        self.points_label.pack()
        self.bank_label = tk.Label(self.master, text=f"Bank: {self.game_state.bank}")
        self.bank_label.pack()

    def make_move(self, divisor):
        if self.game_state.number % divisor == 0:
            new_number = self.game_state.number // divisor
            new_points, new_bank = self.calculate_points_and_bank(new_number, self.game_state.points, self.game_state.bank)
            self.game_state = GameState(new_number, new_points, new_bank)
            self.update_labels()

    def calculate_points_and_bank(self, number, points, bank):
        if number % 2 == 1:
            points += 1
        else:
            points -= 1
        if number % 5 == 0 or number % 10 == 0:
            bank += 1
        return points, bank

    def update_labels(self):
        self.number_label.config(text=f"Current Number: {self.game_state.number}")
        self.points_label.config(text=f"Points: {self.game_state.points}")
        self.bank_label.config(text=f"Bank: {self.game_state.bank}")