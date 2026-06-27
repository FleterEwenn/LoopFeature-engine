from loopfeature.graph import Graph

def test_basics_Graph():
    graph = Graph(lambda x, y : None)
    points = ["p1", "p2", "p3", "p4"]
    graph.add_elements(points)

    assert graph.get_neighbors("p1") == [("p2", None, None)]
    assert sorted(graph.get_neighbors("p3")) == [("p2", None, None), ("p4", None, None)]
    assert sorted(graph.get_neighbors("p2")) == [("p1", None, None), ("p3", None, None)]
    assert graph.get_neighbors("p4") == [("p3", None, None)]

def test_shortest_path_Graph():
    graph = Graph(lambda x, y : 1)
    points = [9, 1, 3, 4, 5, 9, 13]
    graph.add_elements(points)

    graph.construct_dijkstra(3)

    assert graph.get_shortest_path(1) == (1, 3)
    assert graph.get_shortest_path(5) == (2, 4)
    assert graph.get_shortest_path(13) == (3, 9)