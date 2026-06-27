def create_loop(graph, start, dist_max:float, dict_segment:dict)->tuple[list, float]:
        graph.construct_dijkstra(start)
        
        node = start
        passed = [start]
        total_dist = 0
        passed_edge = set()

        while total_dist + graph.get_shortest_path(node)[0] < dist_max:
            print('--------------')
            print(node)
            neighbors = graph.get_neighbors(node)
            best_score = float("-inf")
            best_node = None
            best_dist = 0
            best_edge = None

            ditance_node_to_start = node.calcul_dist(start)

            for neighbor, curr_dist, segment in neighbors:
                distance_neighbor_to_start = neighbor.calcul_dist(start)

                edge = tuple(sorted((node.id, neighbor.id)))

                delta = distance_neighbor_to_start - ditance_node_to_start

                score = segment.score

                score += delta*5

                if edge in passed_edge:
                    score -= 1000
                else:
                    score += 300

                diff = neighbor.elevation - node.elevation
                if neighbor in passed:
                    score -= 500 * passed.count(neighbor)
                else:
                    score += 500
                
                if diff > 0:
                    elevation_gain = diff
                else:
                    elevation_gain = -diff
                score += 100/(abs(30-elevation_gain)+1)
                print(segment.score)
                print(score)
                if score > best_score:
                    best_score = score
                    best_node = neighbor
                    best_dist = curr_dist
                    best_edge = edge
            
            node = best_node
            total_dist += best_dist
            passed.append(node)
            passed_edge.add(best_edge)

        total_dist += graph.get_shortest_path(node)[0]

        while node != start:
            node = graph.get_shortest_path(node)[1]
            passed.append(node)
        
        return passed, total_dist