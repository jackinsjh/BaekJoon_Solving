from collections import deque

def DFS(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            tempList = []
            for i in graph[node]:
                if i not in visited:
                    tempList.append(i)
            tempList.sort(reverse=True)
            for i in tempList:
                stack.append(i)

    visited = map(str, visited)
    print(" ".join(visited))



def BFS(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            tempList = []
            for i in graph[node]:
                if i not in visited:
                    tempList.append(i)
            tempList.sort()
            for i in tempList:
                queue.appendleft(i)

    visited = map(str, visited)
    print(" ".join(visited))





numOfVertices, numOfLines, startPoint = map(int, input().split())

graph = {}

for i in range(numOfLines):
    n1, n2 = map(int, input().split())

    if n1 not in graph:
        graph[n1] = []

    graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = []

    graph[n2].append(n1)

DFS(graph, startPoint)
BFS(graph, startPoint)


