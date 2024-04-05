from typing import List
from collections import namedtuple

from constants import ALLOWED_DIVISORS

GameState = namedtuple("GameState", "number points bank")


class StateNode:

    def __init__(self, game_state: GameState) -> None:
        self.game_state: GameState = game_state

        self.parent: StateNode | None = None
        self.children: List[StateNode] = []

    @property
    def level(self) -> int:
        level = 0
        parent = self.parent
        while parent is not None:
            level += 1
            parent = parent.parent

        return level

    def __str__(self):
        return f'Level: {self.level}, Direct children: {len(self.children)}, State: [number: {self.game_state.number}, points: {self.game_state.points}, bank: {self.game_state.bank}]'

    def add_child(self, child: "StateNode") -> None:
        child.parent = self
        self.children.append(child)


class GameTreeGenerator:

    @staticmethod
    def calculate_points_and_bank(number, points, bank):
        if number % 2 == 1:
            points += 1
        else:
            points -= 1
        if number % 5 == 0 or number % 10 == 0:
            bank += 1
        return points, bank

    @staticmethod
    def generate_tree(game_state: GameState) -> StateNode:

        node = StateNode(game_state)

        for divisor in ALLOWED_DIVISORS:
            if node.game_state.number % divisor == 0:

                new_number = node.game_state.number // divisor
                new_points, new_bank = GameTreeGenerator.calculate_points_and_bank(
                    new_number, node.game_state.points, node.game_state.bank)

                new_state = GameState(new_number, new_points, new_bank)
                new_node = GameTreeGenerator.generate_tree(new_state)
                node.add_child(new_node)

        return node
