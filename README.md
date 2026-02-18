Breath First Search(BFS):- BFS(Graph, S): create empty queue Q mark S as visited enqueue S into Q
while Q is not empty:
    V = dequeue Q
    print V

    for each neighbor U of V:
        if U not visited:
            mark U as visited
            enqueue U into Q
