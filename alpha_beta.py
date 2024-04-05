
from tree_generator import StateNode, GameState

class AlphaBeta:
    @staticmethod
    def alpha_beta(node: StateNode, depth: int, alpha: int, beta: int, maximizing_player: bool) -> int:
        if depth == 0 or len(node.children) == 0:
            return AlphaBeta.heuristic(node.game_state)

        if maximizing_player:
            value = float("-inf")
            for child in node.children:
                value = max(value, AlphaBeta.alpha_beta(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float("inf")
            for child in node.children:
                value = min(value, AlphaBeta.alpha_beta(child, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    @staticmethod
    def heuristic(game_state: GameState) -> int:
        heuristic_value = 0
        if game_state.number % 2 == 1:
            heuristic_value += 1
        else:
            heuristic_value -= 1
        if game_state.number % 5 == 0 or game_state.number % 10 == 0:
            heuristic_value += 1
        return heuristic_value

