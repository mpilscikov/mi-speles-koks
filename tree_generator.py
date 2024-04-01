from typing import List, Literal
from collections import namedtuple

from constants import ALLOWED_DIVISORS

GameState = namedtuple("GameState", "number points bank")


class StateNode:

    def __init__(self, game_state: GameState, heuristic_value) -> None:
        self.game_state: GameState = game_state

        self.parent: StateNode | None = None
        self.children: List[StateNode] = []
        self.heuristic_value: int = heuristic_value

    @property
    def level(self) -> int:
        level = 0
        parent = self.parent
        while parent is not None:
            level += 1
            parent = parent.parent

        return level

    def __str__(self):
        return f'Level: {self.level}, Value: {self.heuristic_value}, Direct children: {len(self.children)}, State: [number: {self.game_state.number}, points: {self.game_state.points}, bank: {self.game_state.bank}]'

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
    def generate_tree(game_state: GameState, heuristic_value: int, ai_player: Literal[1, 2]) -> StateNode:

        node = StateNode(game_state, heuristic_value)

        for divisor in ALLOWED_DIVISORS:
            if node.game_state.number % divisor == 0:

                new_number = node.game_state.number // divisor
                new_points, new_bank = GameTreeGenerator.calculate_points_and_bank(
                    new_number, node.game_state.points, node.game_state.bank)

                new_state = GameState(new_number, new_points, new_bank)
                new_heuristic_value = GameTreeGenerator._calculate_heuristic_value(
                    node, new_state, ai_player)
                new_node = GameTreeGenerator.generate_tree(
                    new_state, new_heuristic_value, ai_player)
                node.add_child(new_node)

        return node

    @staticmethod
    def _calculate_heuristic_value(
            parent_node: StateNode, game_state: GameState, ai_player: Literal[1, 2]) -> int:

        if parent_node is None:
            return 0

        finish_points = game_state.points

        if game_state.points % 2 == 0:
            finish_points += game_state.bank
        else:
            finish_points -= game_state.bank

        if (ai_player == 1 and finish_points % 2 == 1) or (ai_player == 2 and finish_points % 2 == 0):
            return parent_node.heuristic_value + 1

        return parent_node.heuristic_value
