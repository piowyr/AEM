from typing import List
import numpy as np # type: ignore
import matplotlib.pyplot as plt
import networkx as nx

Solution = List[int]

class Visualizer:

    def __init__(self):
        self.graph = None
        self.graph_image = None

    def create_graph(self, solution: Solution, matrix: np.ndarray) -> None:
        rows, cols = np.where(matrix > 0)
        points_a = solution.copy()[:-1]
        points_b = solution.copy()[1:]
        edges = zip(points_a, points_b)
        gr = nx.Graph()
        gr.add_edges_from(edges)
        nx.draw(gr, node_size=100)
        plt.show()

    def create_graph_euclidean(self, solution: Solution, matrix: np.ndarray,
                               vertices: List[List[int]]) -> None:
        vertices = np.array(vertices)
        plt.plot(vertices[:, 0], vertices[:, 1], "o")
        points_a = solution.copy()[:-1]
        points_b = solution.copy()[1:]
        points_a = vertices[points_a]
        points_b = vertices[points_b]
        for a, b in zip(points_a, points_b):
            plt.plot([a[0], b[0]], [a[1], b[1]], '-')
        plt.show()

        # background = Image.new('RGB', (900, 900), (255, 255, 255))
        # draw = ImageDraw.Draw(background)
        # for point in 
        # draw.ellipse((20, 20, 80, 80), fill = 'blue', outline ='blue')
        # del draw
        # background.show()

    def save_graph(self, graph=None) -> None:
        pass