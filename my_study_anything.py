# # 인접리스트 만들기
# graph = [[] for i in range(10)]
#
# graph[0].append((1,7))
# graph[0].append((2,5))
#
# graph[1].append((0,7))
#
# graph[2].append((2,4))
#
# print(graph)

# DFS 정의

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)