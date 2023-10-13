graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start_node):
    queue = []
    visited = set()
    queue.append(start_node)
    visited.add(start_node)
    while queue:
        current_vertex = queue.pop(0)
        print(current_vertex)

        for neighbour in graph[current_vertex]:
            if neighbour not in visited :
                queue.append(neighbour)
                visited.add(neighbour)
bfs(graph, "A")


       

        




