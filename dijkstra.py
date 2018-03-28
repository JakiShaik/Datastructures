from heapdict import heapdict
from collections import defaultdict

def shortest(num_nodes,_edges):
    nodes_heapdct = heapdict()
    nodes_heapdct[0] = 0
    degree = defaultdict(int)
    for i in range(1,num_nodes):
        nodes_heapdct[i] = 99999999
    edges = defaultdict(list)
    for (u,v,w) in _edges:
        edges[u].append((v,w))
        degree[v] += 1
    for i in range(num_nodes):
        if i not in degree:
            degree[i] = 0
    print(degree)
    back = defaultdict(int)
    while len(nodes_heapdct) > 0:
        small = nodes_heapdct.popitem()
        print('small is '+str(small))
        if degree[small[0]] == 0:
            print('degree is zero')
            for connections in edges[small[0]]:
                degree[connections[0]] -= 1
                if (small[1] + connections[1] < nodes_heapdct[connections[0]]):
                    nodes_heapdct[connections[0]] = small[1] + connections[1]
                    back[connections[0]] = small[0]
        else:
            nodes_heapdct[small[0]] = small[1]
    result = small[1]
    res = []
    res.append(small[0])
    req = small[0]
    while req in back:
        res.append(back[req])
        req = back[req]
    res = res[::-1]
    return result,res
#print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
#print(shortest(4,[(0,1,1), (0,2,5), (1,2,7), (2,3,2), (1,3,6)]))
print(shortest(7,[(0,1,0), (0,2,1), (0,3,2),(1,4,1), (2,4,2),(2,5,2),(3,5,1),(4,6,1),(5,6,2)]))
