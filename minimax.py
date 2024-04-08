from tree_generator import StateNode, GameState


class Minimax:
    @staticmethod
    def minimax(node: StateNode, depth: int, maximizing_player: bool, firstPlayer: str) -> int:
        # <------------- for debugging ------------->
        print(str(node))

        if depth == 0 or not node.children:
            # <------------- for debugging ------------->
            print(Minimax.heuristic(node.game_state, firstPlayer))
            return Minimax.heuristic(node.game_state, firstPlayer)

        if maximizing_player:
            best_num = float("-inf")
            for child in node.children:
                value = Minimax.minimax(child, depth - 1, False, firstPlayer)
                best_num = max(best_num, value)
            return best_num
        else:
            best_num = float("inf")
            for child in node.children:
                value = Minimax.minimax(child, depth - 1, True, firstPlayer)
                best_num = min(best_num, value)
            return best_num

    @staticmethod
    def heuristic(game_state: GameState, firstPlayer) -> int:
        points = game_state.points
        bank = game_state.bank

        points += bank if points % 2 == 1 else -bank
        bank += 1 if points % 10 in (0, 5) else 0
        points -= bank if points % 2 == 1 else -bank

        if points % 2 == 1:
            if firstPlayer == 1:
                return 1
            else:
                return -1
        else:
            if firstPlayer == 1:
                return -1
            else:
                return 1
