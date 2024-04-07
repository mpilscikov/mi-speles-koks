from tree_generator import StateNode, GameState


class AlphaBeta:
    @staticmethod
    def alpha_beta(node: StateNode, depth: int, alpha: int, beta: int, maximizing_player: bool,
                   firstPlayer: str) -> int:
        # for debugging print(str(node))

        if depth == 0 or len(node.children) == 0:
            # for debugging print(AlphaBeta.heuristic(node.game_state, firstPlayer))
            return AlphaBeta.heuristic(node.game_state, firstPlayer)

        if maximizing_player:
            value = float("-inf")
            for child in node.children:
                value = max(value, AlphaBeta.alpha_beta(child, depth - 1, alpha, beta, False, firstPlayer))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float("inf")
            for child in node.children:
                value = min(value, AlphaBeta.alpha_beta(child, depth - 1, alpha, beta, True, firstPlayer))
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    @staticmethod
    def heuristic(game_state: GameState, firstPlayer) -> int:
        heuristic_value = 0
        if firstPlayer == "Player":
            if (game_state.points + game_state.bank) % 2 == 0:
                heuristic_value += 1
            else:
                heuristic_value -= 1
        else:
            if (game_state.points + game_state.bank) % 2 == 0:
                heuristic_value -= 1
            else:
                heuristic_value += 1
        return heuristic_value
