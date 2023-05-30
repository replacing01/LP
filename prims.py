INF=999999
v=int(input('enter the number of vertices: '))

#G = [[0, 9, 75, 0, 0], [9, 0, 95, 19, 42], [75, 95, 0, 51, 66], [0, 19, 51, 0, 31], [0, 42, 66, 31, 0]]

setMST=[0,0,0,0,0]
g=eval(input('give the ajacency matrix: '))
edges=0

setMST[0]=True
print('\nEdge : Weight')
while edges<v-1:
    minimum=INF
    x=0
    y=0
    for i in range(v):
        if setMST[i]:
            for j in range(v):
                if ((not setMST[j]) and g[i][j]):
                    if minimum>g[i][j]:
                        minimum=g[i][j]
                        x=i
                        y=j
    
    print(str(x)+'->'+str(y)+' : '+str(g[x][y]))
    setMST[y]=True
    edges+=1