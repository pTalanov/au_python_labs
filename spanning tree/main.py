import sys

OPTIMAL_TIME_FOR_ONE_FRAME = 1.0

sys.path.append("../nx/networkx-1.7-py3.2.egg")

import matplotlib.pyplot as plt
import networkx as nx

from kruskal import KruskalAlgorithm
from time import clock, sleep

# labels represent nodes, numbers are weights
graphDescription = {
    ('a', 'b'): 3,
    ('a', 'c'): 2,
    ('c', 'd'): 1,
    ('y', 'z'): 1,
    ('c', 'y'): 3,
    ('d', 'z'): 100,
    ('a', 'y'): 21,
    ('q', 'a'): 100,
    ('v', 'a'): 23,
    ('v', 'x'): -3,
    ('x', 'a'): 5
}

graph = nx.Graph()

for (u, v) in graphDescription:
    graph.add_edge(u, v)

def weights(edge):
    try:
        return graphDescription[edge]
    except KeyError:
        (u, v) = edge
        return graphDescription[(v, u)]


import matplotlib.animation as animation


edgeLabels={}
for (u, v) in graph.edges():
    edgeLabels[(u, v)] = weights((u, v))

figure = plt.figure()
figure.set_facecolor('white')
pos=nx.spring_layout(graph)

def drawGraph(currentSpanningTreeEdges):
    plt.clf()
    plt.axis('off')
    figure.canvas.set_window_title("Kruskal algorithm for finding minimal spanning tree")
    nx.draw_networkx_nodes(graph, pos, node_size = 1000)
    nx.draw_networkx_edges(graph, pos, width=1, edge_color="b", alpha = 0.5)
    nx.draw_networkx_edges(graph, pos, edgelist=currentSpanningTreeEdges, edge_color="g", width=6)
    nx.draw_networkx_labels(graph, pos, font_size=20, font_family='sans-serif')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edgeLabels)

alg = KruskalAlgorithm(graph, weights)

def animate(i):
    global alg
    if i == 0:
        alg = KruskalAlgorithm(graph, weights)

    start = clock()
    drawGraph(alg.getSelectedSpanningTreeEdges())
    alg.nextStep()
    timeShowingThisFrame = clock() - start
    if timeShowingThisFrame < OPTIMAL_TIME_FOR_ONE_FRAME:
        sleep(OPTIMAL_TIME_FOR_ONE_FRAME - timeShowingThisFrame)

ani = animation.FuncAnimation(figure, animate, len(graph.nodes()), repeat=True)
plt.show()