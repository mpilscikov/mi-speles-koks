from tree_generator import StateNode, GameState

class Minimax:
    @staticmethod
    def minimax(node: StateNode, depth: int,  maximizing_player: bool, ai_player: int)-> int:
        if depth == 0 or not node.children:
            return Minimax.heuristic(node.game_state, ai_player)

        if maximizing_player:
            best_num = float("-inf")
            for child in node.children:
                value = Minimax.minimax(child, depth - 1, False, ai_player)
                best_num = max(best_num, value)
            return best_num
        else:
            best_num = float("inf")
            for child in node.children:
                value = Minimax.minimax(child,  depth - 1, True, ai_player)
                best_num = min(best_num, value)
            return best_num 

    @staticmethod
    def heuristic(game_state:GameState, ai_player: int) -> int:
        points = game_state.points
        bank = game_state.bank

        points += bank if points % 2 == 1 else -bank
        bank += 1 if points % 10 in (0, 5) else 0
        points -=  bank if points % 2 == 1 else -bank

        if points % 2 == 1:
            if ai_player == 1:
                return 1
            else:
                return  -1
        else:
            if ai_player == 1:
                return -1
            else:
                return 1 



