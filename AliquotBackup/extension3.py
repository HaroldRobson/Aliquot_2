import networkx as nx
import pygraphviz
import matplotlib.pyplot as plt
from question1 import SOE, S
# This plots the graph of aliquot sequences up to 300; whilst lower numbers can be used (the graph can get a bit crowded), i wanted to include the amicable pair {220, 284} 
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
            tree.add_edge(n, result)
    return tree

# Visualize the tree
def visualize_tree(tree):
    pos = nx.nx_agraph.graphviz_layout(tree, prog="dot")
    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos, with_labels=True, arrows=True, node_size=120, node_color="lightblue", font_size=4)
    plt.title("Tree Diagram of the Function")
    plt.show()

# Usage
max_n = 300 # Set the maximum number to explore
tree = generate_tree(max_n)
visualize_tree(tree)
