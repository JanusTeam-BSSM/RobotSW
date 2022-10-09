import heapq

def dijkstra(graph, first, last):
    path_data = []
    distance = {node:[float('inf'), first] for node in graph}
    distance[first] = [0, first]
    queue = []

    heapq.heappush(queue, [distance[first][0], first])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distance[current_node][0] < current_distance:
            continue

        for next_node, weight in graph[current_node].items():
            total_distance = current_distance + weight

            if total_distance < distance[next_node][0]:
                # 다음 노드까지 총 거리와 어떤 노드를 통해서 왔는지 입력
                distance[next_node] = [total_distance, current_node]
                heapq.heappush(queue, [total_distance, next_node])
    # 마지막 노드부터 첫번째 노드까지 순서대로 출력
    path = last
    path_data.append(last)
    while distance[path][1] != first:
        path_data.append(distance[path][1])
    path_data.append(first)
    path_data.reverse()
    print(path_data)
    return distance

graph = {
    'A': {'B':8, 'C':2, 'D':3},
    'B':{},
    'C':{'B':3, 'D':2},
    'D':{'E':1, 'F':4},
    'E':{},
    'F':{}
}

dijkstra(graph, 'A', 'C')

