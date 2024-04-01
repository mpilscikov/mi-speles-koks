import math


class AlgorithmMinimax:

    def __init__(self, move=None, value=None):
        self.move = move
        self.value = value

    def __str__(self):
        return f" {self.move}: {self.value}"

    def minimax(self,  node, is_max):

        if not node.children:
            return AlgorithmMinimax(None, node.heuristic_value)

        if is_max:
            value_max = -math.inf

            for child in node.children:
                value = self.minimax(child, False).value
                value_max = max(value_max,  value)
            return AlgorithmMinimax("max", value_max)

        else:
            valMin = math.inf

            for child in node.children:
                value = self.minimax(child, True).value
                valMin = min(valMin, value)
            return AlgorithmMinimax("min", valMin)
