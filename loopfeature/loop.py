def create_loop(graph, start, dist_max:float, dict_segment:dict)->tuple[list, float]:
        graph.construct_dijkstra(start)
        
        node = start
        passed = [start]
        total_dist = 0

        while dist + graph.get_shortest_path(node)[0] < dist_max:
            max_score_node = float("-inf")
            for neighbor, curr_dist in graph.get_neighbors(node):
                max_score_segment = float("-inf")
                if neighbor in passed:
                    score = -100
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

        dist += graph.get_shortest_path(node)[0]

        while node != start:
            node = graph.get_shortest_path(node)[1]
            passed.append(node)
        
        return passed, dist