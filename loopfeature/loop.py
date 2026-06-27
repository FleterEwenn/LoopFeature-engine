def create_loop(graph, start, dist_max:float, dict_segment:dict)->tuple[list, float]:
        graph.construct_dijkstra(start)
        
        node = start
        passed = [start]
        total_dist = 0

        while total_dist + graph.get_shortest_path(node)[0] < dist_max:

            dist_node_to_start = start.calcul_dist(node)

            max_score_node = float("-inf")

            neighbors = graph.get_neighbors(node)
            node, dist = neighbors[0]

            for neighbor, curr_dist in neighbors:
                dist_neighbor_to_start = start.calcul_dist(neighbor)

                max_score_segment = float("-inf")
                if neighbor in passed:
                    base_score = -500
                else:
                    base_score = 500
                
                if dist_node_to_start > dist_neighbor_to_start:
                    base_score -= 200
                else:
                    base_score += 200 

                for segment in dict_segment[neighbor.id]:
                    score = base_score + segment.score

                    dist_neighbor_to_first = neighbor.calcul_dist(segment.first_point)
                    dist_neighbor_to_last = neighbor.calcul_dist(segment.last_point)

                    if dist_neighbor_to_last > dist_neighbor_to_first:
                        ratio = segment.elev_gain_FtoL/(segment.distance/1000)
                    else:
                        ratio = segment.elev_gain_LtoF/(segment.distance/1000)
                    score += 100/(abs(30-ratio)+1)

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