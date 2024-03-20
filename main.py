from tree_generator import GameTreeGenerator, GameState

# šis ir kods testēšanai

initial_state = GameState(100000, 0)
tree = GameTreeGenerator.generate_tree(initial_state)

def print_tree(node):
    print(node)
    
    if node.children:
        for child in node.children:
            print_tree(child)
            
print_tree(tree)