import queue


class Graph:
    def __init__(self, nodes_count, directed=True):
        self.nodes_count = nodes_count
        self.directed = directed
        self.adjList = {node: set() for node in range(nodes_count)}

    def add_edge(self, start, end, weight=1):
        self.adjList[start].add((end, weight))
        if not self.directed:
            self.adjList[end].add((start, weight))

    def modify_directed_to_undirected(self):
        self.directed = False
        for start in self.adjList:
            for end, weight in self.adjList[start]:
                if (start, weight) not in self.adjList[end]:
                    self.adjList[end].add((start, weight))

    # returns path from start to target node.
    # returns weight of the path. if all weights are 1, then weight is the distance from start to target node
    def get_shortest_path_from_start(self, start_node, target_node):
        path_found = False
        visited = set()
        parents = dict()
        parents[start_node] = (None, 0)
        q = queue.Queue()
        q.put(start_node)

        while not q.empty():
            node = q.get()
            if node == target_node:
                path_found = True
                break
            visited.add(node)
            for (adj, weight) in self.adjList[node]:
                if adj not in visited:
                    q.put(adj)
                    parents[adj] = (node, weight)
                    visited.add(adj)
        path = []
        weight = 0
        if path_found:
            path.append(target_node)
            while target_node != start_node:
                parent, edge_weight = parents[target_node]
                path = [parent] + path
                weight += edge_weight
                target_node = parent
        return path, weight

    # returns number of connected sub-graphs (components)
    # I'm specifically practicing BFS here. If the graph is directed I will turn it into undirected graph (in O(E)).
    # Other way how to count components of directed graph is by topological sort (shown in different file)
    def get_number_of_components(self):
        self.modify_directed_to_undirected()
        component_count = 0

        # assuming we have nodes from 0 tot self.nodeCount
        not_seen = set()
        for i in range(self.nodes_count):
            not_seen.add(i)

        while len(not_seen) > 0:
            newNode = not_seen.pop()

            # discoverComponent
            q = queue.Queue()
            q.put(newNode)
            while not q.empty():
                node = q.get()
                if node in not_seen:
                    not_seen.remove(node)
                for (adj, weight) in self.adjList[node]:
                    if adj in not_seen:
                        q.put(adj)
            component_count += 1

        return component_count

    # traverse connected undirected graph
    def bfs_component_traversal_for_undirected_graph(self, start_node):
        visited = set()
        q = queue.Queue()
        q.put(start_node)
        traversal = []

        while not q.empty():
            node = q.get()
            traversal.append(node)
            visited.add(node)
            for (adj, weight) in self.adjList[node]:
                if adj not in visited:
                    q.put(adj)
                    visited.add(adj)
        return traversal
