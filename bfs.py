graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

visited=[]
queue=[]

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m, end="\n")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

#driver code
print("The BFS of the graph is:")
bfs(visited, graph, '5')