from typing import Literal
from tree_generator import StateNode

def alpha_beta_search(node: StateNode, depth: int, alpha: int, beta: int, ai_player: Literal[1, 2]) -> int:
    if depth == 0 or not node.children:
        return node.heuristic_value

    if ai_player == 1:
        value = float('-inf')
        for child in node.children:
            value = max(value, alpha_beta_search(child, depth - 1, alpha, beta, ai_player))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alpha_beta_search(child, depth - 1, alpha, beta, ai_player))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

def find_best_move(node: StateNode, depth: int, ai_player: Literal[1, 2]) -> int:
    best_value = float('-inf') if ai_player == 1 else float('inf')
    best_move = -1

    for i, child in enumerate(node.children):
        value = alpha_beta_search(child, depth - 1, float('-inf'), float('inf'), ai_player)
        if ai_player == 1:
            if value > best_value:
                best_value = value
                best_move = i
        else:
            if value < best_value:
                best_value = value
                best_move = i
    return best_move