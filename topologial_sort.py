def dfs(node, graph, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, stack)
    stack.append(node)

def topological_sort(graph):
    visited = {node: False for node in graph}
    stack = []
    for node in graph:
        if not visited[node]:
            dfs(node, graph, visited, stack)
    return stack[::-1]


graph = {
    1: [2, 5],
    2: [3],
    3: [4],
    4: [],
    5: [2, 6],
    6: [4]
}


topological_sort(graph)

