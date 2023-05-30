graph = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visited=[]

def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        print(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

#Driver Code
print('Following is the DFS: ')
dfs(visited, graph, '5')