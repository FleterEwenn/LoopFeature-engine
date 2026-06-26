def create_loop(graph, start, dist_max:float, dict_segment:dict)->tuple[list, float]:
        graph.construct_dijkstra(start)
        
        node = start
        passed = [start]
        total_dist = 0

        while total_dist + graph.get_shortest_path(node)[0] < dist_max:
            max_score_node = float("-inf")

            neighbors = graph.get_neighbors(node)
            node, dist = neighbors[0]

            for neighbor, curr_dist in neighbors:
                max_score_segment = float("-inf")
                if neighbor in passed:
                    score = -500*passed.count(neighbor)
                else:
                    score = 100

                for segment in dict_segment[neighbor.id]:
                    score += segment.score
                    if score > max_score_segment:
                         max_score_segment = score
                
                if max_score_segment > max_score_node:
                    max_score_node = max_score_segment
                    dist = curr_dist
                    node = neighbor

            total_dist += dist
            passed.append(node)

        total_dist += graph.get_shortest_path(node)[0]

        while node != start:
            node = graph.get_shortest_path(node)[1]
            passed.append(node)
        
        return passed, total_dist