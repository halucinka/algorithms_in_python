import math
from unittest import TestCase

from algorithms_in_python.dijkstra.graph_as_matrix.main import getShortestDistancesFromVertex


class Test(TestCase):
    def test_get_shortest_distances_from_vertex(self):
        graph = [[0, 1, 1],
                 [1, 0, 0],
                 [1, 0, 0]]
        self.assertEqual([0, 1, 1], getShortestDistancesFromVertex(graph, 0))

        graph = [[0, 1, 1, 0],
                 [1, 0, 1, 0],
                 [1, 0, 0, 1],
                 [0, 0, 1, 0]]
        self.assertEqual([0, 1, 1, 2], getShortestDistancesFromVertex(graph, 0))

        graph = [[0, 1, 0, 0],
                 [1, 0, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]]
        self.assertEqual([0, 1, math.inf, math.inf], getShortestDistancesFromVertex(graph, 0))

        graph = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        self.assertEqual([0, math.inf, math.inf, math.inf], getShortestDistancesFromVertex(graph, 0))
