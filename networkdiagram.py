import networkx as nx
import pygraphviz
import matplotlib.pyplot as plt
from question_1 import SOE, S
# Example function
onlyprimes = []
prime_dict = {}
SOE(10000)
def f(n):
    if n == 0:
        return None  # 0 is the end of the tree
    if n != 0:
        return S(n)

# Generate the tree
def generate_tree(max_n):
    tree = nx.DiGraph()
    for n in range(max_n + 1):
        result = f(n)
        if result is not None:
            tree.add_edge(result, n)
    return tree

# Visualize the tree
def visualize_tree(tree):
    pos = nx.nx_agraph.graphviz_layout(tree, prog="dot")
    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos, with_labels=True, arrows=True, node_size=3000, node_color="lightblue", font_size=10)
    plt.title("Tree Diagram of the Function")
    plt.show()

# Usage
max_n = 50 # Set the maximum number to explore
tree = generate_tree(max_n)
visualize_tree(tree)
