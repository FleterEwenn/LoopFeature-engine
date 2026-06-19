from overpass import get_path
from dijkstra import dijkstra
from graphe_manage import create_graphe, create_loop
from generate_GPX import generate_GPX
import time
import random

list_path = False

while not list_path:
    list_path = get_path()
    time.sleep(0.1)

graphe = create_graphe(list_path)
start = list(graphe.keys())[random.randint(0, 3058)]
#start = (round(45.0251272, 5), round(1.7876748, 5))
shortly_distance = dijkstra(graphe, start)

with open("dijkstra.txt", "w") as f:
    f.write(str(shortly_distance))
with open("graphe.txt", "w") as f:
    f.write(str(graphe))

loop_path = create_loop(start, shortly_distance, graphe, 15000)

print(loop_path[1])

with open("path.txt", "w") as f:
    f.write(str(loop_path[0]))

generate_GPX(loop_path[0])