#!/usr/bin/python




V = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

E = [('a', 'b'), ('a', 'e'), ('a', 'f'), ('b', 'c'), ('c', 'f'),
     ('d', 'e'), ('d', 'f'), ('d', 'g'), ('e', 'f'), ('e', 'g')]

cVal = {('a', 'b'): 8, ('a', 'e'): 3, ('a', 'f'): 1, ('b', 'c'): 2,
        ('c', 'f'): 3, ('d', 'e'): 7, ('d', 'f'): 5, ('d', 'f'): 5,
        ('d', 'g'): 2, ('e', 'f'): 4, ('e', 'g'): 1}


def printPath(v):
    arr = []
    path = ''
    while (p[v] != SOURCE):
        arr.insert(0, p[v])
        v = p[v];
    arr.insert(0, SOURCE)
    for i in arr:
        path += i + '-'
    return (path[:-1])

def c(u, v):
    if (u, v) in cVal:
        return cVal[(u, v)]
    elif (v, u) in cVal:
        return cVal[(v, u)]


def findNeighbor(v):
    arr = []
    for (a, b) in E:
        if (a == v):
            arr.append(b)
        elif (b == v):
            arr.append(a)
    arr = set(arr)
    return arr


for SOURCE in V:

    # cost of the least-cost path from the source node to destination v as of this iteration of the algorithm.
    D = {}
    p = {SOURCE:SOURCE}
    nTag = [SOURCE]

    # init#

    '''init the first p(v) with the neighbor of the source vertex'''
    for v in findNeighbor(SOURCE):
        p[v]=SOURCE

    '''init the distance between the source and his neigbhors'''
    for v in V:
        if (SOURCE, v) in E:        # if v is neighbor of source
            D[v] = c(SOURCE, v)
        elif (v, SOURCE) in E:       # if source is a neighbor of v
            D[v] = c(v,SOURCE)
        else:
            D[v] = 9999             #else the dis is init to infinity
    #end init

    while set(V) != set(nTag):
        '''looking for the least coast path for any vertex that not apper in nTag'''
        mini = 9999
        w = ''
        for vertex in V:
            if vertex not in nTag:
                if (D[vertex] < mini):
                    mini = D[vertex]
                    w = vertex
        nTag.append(w)

        for v in findNeighbor(w):
            if v not in nTag:
                if(D[w]+c(w, v)<=D[v]):
                    p[v] = w
                    D[v] = D[w] + c(w, v)
                else:
                    p[v]=p[w]
            ''' new cost to v is either old cost to v or known
                least path cost to w plus cost from w to v '''

    for v in V:
        path=""
        if v != SOURCE:
            print('<' + SOURCE +': ' + v +', <'+ printPath(v)+">, "+str(D[v])+'>' )
    print('\n')


