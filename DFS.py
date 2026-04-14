
graph = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3]
}
def dfs(start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()   
        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

dfs(1)
