def dfs(graph, v, visited):
    visited[v]=True # 현재 노드를 방문 처리
    print(v, end=' ')
  
    for i in graph[v]: # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i, visited)
            
graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]] 
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)

visited=[False]*9 # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)

dfs(graph,1,visited)
