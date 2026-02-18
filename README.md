Breath First Search(BFS):- BFS(Graph, S): create empty queue Q mark S as visited enqueue S into Q
while Q is not empty:
    V = dequeue Q
    print V

    for each neighbor U of V:
        if U not visited:
            mark U as visited
            enqueue U into Q


DEPTH FIRST SEARCH(DFS):- DFS(Graph):
for each vertex V in Graph:
    mark V as not visited

for each vertex V in Graph:
    if V is not visited:
        DFS_Visit(V)

DFS_Visit(V):
mark V as visited
print V

for each neighbor U of V:
    if U is not visited:
        DFS_Visit(U)


UNIFORM COST SEARCH(UCS):- UCS(Graph, Start, Goal):

create priority queue PQ
create cost table

cost(Start) = 0
insert Start into PQ

while PQ not empty:

    Current = extract node with minimum cost

    if Current == Goal:
        stop

    for each neighbor N of Current:

        tempCost = cost(Current) + edgeCost(Current, N)

        if N not visited OR tempCost < cost(N):
            cost(N) = tempCost
            parent(N) = Current
            insert N into PQ


GREEDY BREATH FIRST SEARCH (GBFS):- GBFS(Graph, Start, Goal):

create OPEN priority queue (based on heuristic h(n))
create CLOSED set

insert Start into OPEN

while OPEN not empty:

    Current = extract node with minimum h(n)

    if Current == Goal:
        stop

    move Current to CLOSED

    for each neighbor N of Current:
        if N not in CLOSED:
            parent(N) = Current
            insert N into OPEN



A* SEARCH:-

Insert Start node into OPEN

Compute f(n) = g(n) + h(n)

Repeat until Goal reached:

a. Select node with smallest f(n) b. If Goal → Stop c. Expand neighbors d. Update g(n) and f(n)

WATER JUG SEARCH:- WaterJugProblem(Capacity1, Capacity2, Target):

create empty queue Q
create VISITED set

initial_state = (0, 0)
enqueue initial_state into Q
mark initial_state as visited

while Q is not empty:

    (x, y) = dequeue Q

    if x == Target OR y == Target:
        print solution
        stop

    generate next possible states:

        1. Fill Jug1 → (Capacity1, y)
        2. Fill Jug2 → (x, Capacity2)
        3. Empty Jug1 → (0, y)
        4. Empty Jug2 → (x, 0)
        5. Pour Jug1 → Jug2
        6. Pour Jug2 → Jug1

    for each new_state:
        if new_state not visited:
            enqueue new_state into Q
            mark new_state as visited



MIN-MAX SEARCH:- Minimax(node, depth, isMaxPlayer):

if node is terminal OR depth == 0:
    return value(node)

if isMaxPlayer:

    bestValue = -∞

    for each child of node:
        value = Minimax(child, depth - 1, false)
        bestValue = max(bestValue, value)

    return bestValue

else:

    bestValue = +∞

    for each child of node:
        value = Minimax(child, depth - 1, true)
        bestValue = min(bestValue, value)

    return bestValue



ALPHA BETA SEARCH:- ALPHA_BETA(node, depth, alpha, beta, isMax):

if terminal(node) OR depth == 0:
    return heuristic(node)

if isMax:
    value = -∞
    for child in children(node):
        value = max(value,
                    ALPHA_BETA(child, depth-1, alpha, beta, false))
        alpha = max(alpha, value)
        if alpha >= beta:
            break       // beta cut-off
    return value

else:
    value = +∞
    for child in children(node):
        value = min(value,
                    ALPHA_BETA(child, depth-1, alpha, beta, true))
        beta = min(beta, value)
        if beta <= alpha:
            break       // alpha cut-off
    return value
