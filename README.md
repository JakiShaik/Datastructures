# Datastructures
CS519-010-Algorithms
  codebeat badge

homeworks
sort
heap
DP and Graph
knapsack
BFS and DFS
graph algorithm comparison
priority queue(PQ) implememtations for Dijkstra
HW1: Python 3, qsort, BST, and qselect
code and description [10/10 cases] Total Time: 0.083 s

HW2: Divide-n-conquer: mergesort, number of inversions, longest path
code and description [10/10 cases] Total Time: 0.377 s

HW3: K closest numbers; Two Pointers
code and description [10/10 cases] Total Time: 0.276 s

HW4: Priority Queue and Heaps
code and description [10/10 cases] Total Time: 0.288 s

HW5: DP (part 1: simple)
code and description [10/10 cases] Total Time: 0.009 s

HW6: DP (part 2)
code and description [10/10 cases] Total Time: 0.067 s

HW7: Void (Midterm Week)
HW8: DP (part 3), Graph Algorithms (part 1)
code and description [10/10 cases] Total Time: 0.269 s

HW9: Graph Algorithms (part 2), DP (part 4)
code passed but not uploaded [10/10 cases] Total Time: 0.769 s

HW10: Challenge Problem - RNA Structure Prediction (6%)
code passed but not uploaded [25/25 cases] Total Time: 0.592 s

Back to Contents CS 519-010

sort
01/11/2018 Thu
+	qsort	qselect	bsearch	msort
1.divide	O(n)	O(n)	O(1)	O(1)
2.conquer	2x	x	x	2x
3.combine	O(n)	O(1)	O(1)	O(n)
worst	O(n^2)	O(n^2)	O(logn)	O(nlogn)
best	O(nlogn)	O(n)	O(logn)	O(nlogn)
ave	O(nlogn)	O(n)	O(logn)	O(nlogn)
list in python is more like vectore in C++, the combination list+list costs O(n)

Back to Contents CS 519-010

heap
01/25/2018 Thu
+	sorted
array	unsorted
array	(binary)
heap	sorted
linked list	unsorted
linked list	reverse-
sorted array
insert	O(n)	O(1)	O(logn)	O(n)	O(1)	O(n)
pop-min	O(n)	O(n)	O(logn)	O(1)	O(n)	O(1)
peak	O(1)	O(n)	O(1)	O(1)	O(n)	O(1)
decrease-key	O(n)	O(n)	O(logn)			
heapify	O(nlogn)	O(1)	O(n)	O(nlogn)	O(1)	O(nlogn)
Back to Contents CS 519-010

DP and graph
02/08/2018 Thu
+	optimization	summary
graph	MIS
max,min
maxmin
Unbunded	(sum, expectation)
Fib
bitstrings
hyperGraph	matrix-chain	# of BSTs
Number of n-node BSTs problem is a hyperpraph problem


Back to Contents CS 519-010

knapsack
02/13/2018 Tue
knapsack problem(W, vi,wi,[ci]):

0-1 knapsack
Unbunded knapsack
Bouded knapsack
All the weights are intergers

1. Unbunded knapsack
approach:
Subproblem
opt[x]: the subsolution for a bag of x
Recurrence
opt[x]=max{ opt[x-w[i]]+v[i] }, i=0..n-1 and x>=w[i]
base case
opt[0] = 0
Unbunded is a graph problem
time = E(edges) = O(nW)
space = V(node) = O(W)
topological order in graph
recursive method(top-down) can automaticly avoid useless value x's without gcd
2. 0-1 knapsack
approach:
Subproblem
opt[i][x]: opt value for a bag of x, using items 0~i
Recurrence
opt[i][x]=max{ opt[i-1][x-w[i]]+v[i], opt[i-1][x] }, i=0~n-1 and x>=w[i]
max { choose i, not choose i }
base case
opt[i][0] = 0, i=0~n-1
opt[-1][x] = 0, x=0~W
Bounded is a graph problem
time = E(edges) = O(nW)
space = V(node) = O(nW)
2 nested for loops(i,x), no matter the order of i/x
in top-down method, order doesn't matter


Back to Contents CS 519-010

BFS and DFS
03/01/2018 Thu
+	BFS	DFS
structure	queue	stack
topological order	bottom-up	top-down
start from	source	sink
Back to Contents CS 519-010

graph algorithm comparison
03/01/2018 Thu
+	Viterbi	Dijkstra
restriction	DAG
(BIG restriction)	non-gegative weights
advantage	fast	works in undirected graph
works in acyclic/cylic gragh
could have early termination
usage	longest/shortest/
number/minmax	shortest path 
single source (s to any)
implementation	topological sort+
BFS(queue)	best-first
(priority queue) 
with decrease key
time complexity	O(V+E)	O((V+E)logV)
common	coin problem, TSP	coin problem, TSP
Back to Contents CS 519-010

priority queue(PQ) implememtations for Dijkstra
03/06/2018 Tue
make your window of browser  as you can
+	PQ
(heapdict)	PQ
(hash)	PQ
(heap)	PQ
(unsorted list)
implementation	binary heap
(heapdict)	hash	binary heap	unsorted list
operatrions	pop-min: logV
push: logV 
decrease-key: logV	pop-min: V
push: O(1) 
decrease-key: O(1)	pop-min: logE
push: logE 
decrease-key: logE	pop-min: V
push: O(1) 
decrease-key: V
time complexity	O((V+E)logV) ↘	O(V^2+E) ↓	O((V+E)logE) ↘	V^2+EV ↓
while PQ not empty:
1. u = pop()
2. for each u->v in E:
2.1 decrease-key	V -----------→ VlogV
logV --------↗ +
e---→ elogV → ElogV
logV↗	V ---→ V^2
V ---↗ +
e→ e → E
1 ↗	V -----------→ VlogE
logE --------↗ +
e---→ elogV → ElogE
logE↗	V ---→ V^2
V ---↗ +
e→eV→EV
V ↗
usage	sparse map
E~V	dense map
E~ ϴ(V^2)		
dense
E~ ϴ(V^2)	V^2logV	V^2 (★)	V^2logV	V^3
sparse
E~V	VlogV (★)	V^2	VlogV	V^2
sparse
E~VlogV	Vlog^2(V) (★)	V^2		
Back to Contents CS 519-010

RNA problem
k-best
tree structure for k-best
