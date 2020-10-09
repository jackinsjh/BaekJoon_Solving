

"""
n, m = map(int, input().split())

visited = []
stack = []

for first in range(1, n + 1):
    stack = []
    stack.append(first)
    visited.append(first)

    while stack:
        for curNode in range(1, n + 1):
            if curNode not in visited:
                stack.append(curNode)
                visited.append(curNode)
                if len(stack) == m:
                    print(" ".join(map(str, stack)))
                    stack.pop()
                    visited.pop()
"""

def DFS(depth):
    if depth == m:
        print(" ".join(visited))

    else:



n, m = map(int, input().split())

visited = []
stack = []





"""
-재귀함수

만약 깊이 만족시 -> 출력

아니라면 ->
for 문으로 visit 되지 않은 점 하나씩 넣고
다시 DFS

"""

https://www.acmicpc.net/problem/15649
https://wlstyql.tistory.com/56