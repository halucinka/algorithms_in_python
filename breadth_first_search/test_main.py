import unittest
from unittest import TestCase

from main import Graph


class TestBinarySearch(unittest.TestCase):

    def test_get_shortest_path_from_start(self):
        # available path, base case
        graph = Graph(2, directed=False)
        graph.add_edge(0, 1)
        self.assertEqual(graph.get_shortest_path_from_start(1, 0), ([1, 0], 1))

        # same test case as ^, no path if graph is directed
        graph = Graph(2, directed=True)
        graph.add_edge(0, 1)
        self.assertEqual(graph.get_shortest_path_from_start(1, 0), ([], 0))

        # no path
        graph = Graph(3, directed=False)
        graph.add_edge(0, 1)
        self.assertEqual(graph.get_shortest_path_from_start(0, 2), ([], 0))

        # weighted
        graph = Graph(2, directed=True)
        graph.add_edge(0, 1, 47)
        self.assertEqual(graph.get_shortest_path_from_start(0, 1), ([0, 1], 47))

        # 0 --> 1 --> 2
        #       |     ^
        #       v     |
        # 3 <-- 4 <-- 5     6
        graph = Graph(7, directed=True)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(1, 4)
        graph.add_edge(5, 2)
        graph.add_edge(4, 3)
        graph.add_edge(5, 4)

        self.assertEqual(graph.get_shortest_path_from_start(0, 1), ([0, 1], 1))
        self.assertEqual(graph.get_shortest_path_from_start(0, 3), ([0, 1, 4, 3], 3))
        self.assertEqual(graph.get_shortest_path_from_start(0, 5), ([], 0))
        self.assertEqual(graph.get_shortest_path_from_start(5, 3), ([5, 4, 3], 2))
        self.assertEqual(graph.get_shortest_path_from_start(5, 7), ([], 0))

        # identical example but UNdirected
        # 0 -- 1 -- 2
        #      |    |
        # 3 -- 4 -- 5    6
        graph = Graph(7, directed=False)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(1, 4)
        graph.add_edge(5, 2)
        graph.add_edge(4, 3)
        graph.add_edge(5, 4)

        self.assertEqual(graph.get_shortest_path_from_start(0, 1), ([0, 1], 1))
        self.assertEqual(graph.get_shortest_path_from_start(1, 0), ([1, 0], 1))
        self.assertEqual(graph.get_shortest_path_from_start(0, 3), ([0, 1, 4, 3], 3))
        self.assertEqual(graph.get_shortest_path_from_start(3, 0), ([3, 4, 1, 0], 3))
        self.assertEqual(graph.get_shortest_path_from_start(2, 5), ([2, 5], 1))
        self.assertEqual(graph.get_shortest_path_from_start(5, 3), ([5, 4, 3], 2))
        self.assertEqual(graph.get_shortest_path_from_start(5, 7), ([], 0))


class TestGraph(TestCase):
    def test_get_number_of_components(self):
        graph = Graph(2, directed=False)
        graph.add_edge(0, 1)
        self.assertEqual(graph.get_number_of_components(), 1)

        graph = Graph(6, directed=False)
        graph.add_edge(0, 1)
        self.assertEqual(graph.get_number_of_components(), 5)

        graph = Graph(3, directed=True)
        graph.add_edge(1, 0)
        self.assertEqual(graph.get_number_of_components(), 2)


class TestGraph(TestCase):
    def test_modify_directed_to_undirected(self):
        graph = Graph(3, directed=True)
        graph.add_edge(1, 0, 47)
        graph.modify_directed_to_undirected()
        self.assertEqual(graph.adjList[0], {(1, 47)})


class TestGraph(TestCase):
    def bfs_component_traversal_for_undirected_graph(self):
        # 0 -- 1 -- 2
        #      |    |
        # 3 -- 4 -- 5
        graph = Graph(6, directed=False)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(1, 4)
        graph.add_edge(5, 2)
        graph.add_edge(4, 3)
        graph.add_edge(5, 4)

        self.assertEqual(len(graph.bfs_component_traversal_for_undirected_graph()), 6)