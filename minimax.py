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
            valMax = -math.inf 

            for child in node.children:
                value = self.minimax(child, False).value
                valMax = max(valMax,  value) 
            return AlgorithmMinimax("max", valMax)  
        
        else:
            valMin = math.inf

            for child in node.children:
                value = self.minimax(child, True).value
                valMin =  min(valMin, value)
            return AlgorithmMinimax("min", valMin)
