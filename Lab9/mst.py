#Imports heapify, heappop, and heappush from the heapq module
from heapq import heapify, heappop, heappush
#Makes a graph class
class Graph:
    #Initializes the graph object
    def __init__(self):
        #This creates a list to store vertex objects
        self.v = []
        #This creates a dictionary to store adjacency lists
        self.adj = dict()
#Makes a node class
class Node:
    #Initializes value
    def __init__(self, value):
        #Related to the value of the node
        self.value = value
        #Related to the parent of the node
        self.parent = None
        #Related to the ranking of the node
        self.rank = 0
        #Related to the key of the node
        self.key = float("inf")
    #Magic method for determining less than
    def __lt__(self, other):
        #Returns True or False depending on the comparison
        return self.key < other.key
    #Magic method to return a printable representation of the object
    def __repr__(self):
        #Returns the printable representation
        return self.value
    #Magic method for determining equal to
    def __eq__(self, other):
        #Runs if "other" is an instance of the Node class
        if isinstance(other, Node):
            #Returns True or False depending on the comparison
            return self.value == other.value
    #Takes one object as an argument and returns the hash value as an integer
    def __hash__(self):
        #Returns the hash value as an integer
        return hash(self.value)
#Creates a new set whose only member (and thus representative) is the value (if the value doesn’t already belong to another set)
def makeSet(value):
    #Assigns node to the value of the node
    node = Node(value)
    #Assign the parent of the current node to the node
    node.parent = node
    #Return the node
    return node
#Merges the two sets containing elements x and y, respectively. Does this through the link function
def union(x, y):
    #Finds the roots of the two trees using findSet(x) and findSet(y)
    link(findSet(x), findSet(y))
#This is responsible for merging the two sets. This is used by the union function. This is the only place where the rank of a tree may be updated
def link(x, y):
    #If the ranking of x is greater than y, this will run
    if x.rank > y.rank:
        #This makes y a child of x, since x has a higher rank
        y.parent = x
    #Otherwise this will run
    else:
        #Makes x a child of y
        x.parent = y
        #If the ranking of x and y are equal, this will run
        if x.rank == y.rank:
            #Increases the rank of y by one
            y.rank = y.rank + 1
#Returns the representative of the set containing element x
def findSet(x):
    #Not the root?
    if x != x.parent:
        #The root becomes the parent
        x.parent = findSet(x.parent)
    #Return the root
    return x.parent
'''
Kruskal's algorithm is implemented by using a disjoint-set data structure, where each set represents a tree
in the forest, and the trees are gradually merged to form the MST. And, the set of edges are 
sorted initially in increasing order of weight and processed one by one
'''
def mstKruskal(G, w):
    #Initialize an empty dictionary to store disjoint sets
    sets = {}
    #Initialize an empty list to store edges
    kruskalEdges = []
    #Sort edges by weight
    edges = sorted(w.keys(), key = lambda x : w[x])
    #Initialize MST weight
    kruskalWeight = 0
    #This will run for every vertex in the graph
    for v in G.v:
        #Create a disjoint set
        sets[v] = makeSet(v)
    #This will run for every edge in the set of edges
    for edge in edges:
        #Unpack
        u, v = edge
        #If the edge's two vertices belong to two different trees, this will run
        if findSet(sets[u]) != findSet(sets[v]):
            #Add the edge to the MST
            kruskalEdges.append(edge)
            #Increase the weight
            kruskalWeight += w[edge]
            #Merge the two trees
            union(findSet(sets[u]), findSet(sets[v]))
    #Return the edges in the MST and the total MST weight
    return kruskalEdges, kruskalWeight
'''
Prim's algorithm at any time always maintains a single tree "A", which will eventually grow to form the MST.
The tree starts from an arbitrary root vertex "r". In each iteration, it adds to tree "A" a minimum-weight edge that
connects the tree to the rest of the vertices. The process repeats until all vertices are added to the tree
'''
def mstPrim(G, w, r):
    #Initializes a a min-priority queue of all vertices that are not already in the tree
    Q = []
    #Initialize an empty list to store edges
    primEdges = []
    #Initialize MST weight
    primWeight = 0
    #This will run for every vertex in the graph
    for u in G.v:
        #Initialize key
        u.key = float("inf")
        #Initialize parent
        u.parent = None
    #Ensures that the root vertex "r" is the first to be extracted from "Q" and added to the tree "A"
    r.key = 0
    #This will run for every vertex in the graph
    for u in G.v:
        #Populate priority queue with all vertices
        heappush(Q, u)
    #Loops for MST creation
    while Q:
        #Add u to the tree
        u = heappop(Q)
        #Update keys of u's non-tree neighbors
        for v in G.adj[u]:
            #Get the weight of edge (u, v)
            tempVar = w.get((u, v))
            #If the edge weight (u, v) is not present, use the weight of the edge (v, u)
            weight = w[(v, u)] if tempVar is None else tempVar
            #Once "u" is added to the tree, possibly update each of its neighbor "v" key and parent
            if v in Q and weight < v.key:
                #Update the parent
                v.parent = u
                #Update the key
                v.key = weight
                #Reorganize the priority queue
                heapify(Q)
    #This will run for every vertex in the graph
    for u in G.v:
        #If the vertex has a parent, this will run
        if u != u.parent:
            #Search the neighbors of u
            for v in G.adj[u]:
                #If v is the parent of u, this will run
                if v == u.parent:
                    #Get the weight of the edge
                    tempVar = w.get((u, u.parent))
                    #If the edge weight (u, v) is not present, use the weight of the edge (v, u)
                    weight = w[(u.parent, u)] if tempVar is None else tempVar
                    #Add the edge to the MST
                    primEdges.append((u, u.parent))
                    #Increase the weight
                    primWeight += weight
                    #Break the loop
                    break
    #Return the edges in the MST and the total MST weight
    return primEdges, primWeight
#Creates a method that will use the different functions to print out their discoveries
def execute():
    #Assigns G to a graph
    G = Graph()
    #Create nodes for the graph
    a = Node("a")
    #Create nodes for the graph
    b = Node("b")
    #Create nodes for the graph
    c = Node("c")
    #Create nodes for the graph
    d = Node("d")
    #Create nodes for the graph
    e = Node("e")
    #Create nodes for the graph
    f = Node("f")
    #Create nodes for the graph
    g = Node("g")
    #Create nodes for the graph
    h = Node("h")
    #Create nodes for the graph
    i = Node("i")
    #Add the nodes to the list of vertices
    G.v = [a, b, c, d, e, f, g, h, i]
    #Assign weights to the edges
    weight = {(a, b): 4, (a, h): 8, (b, c): 8, (b, h): 11, 
              (c, d): 7, (c, f): 4, (c, i): 2, (d, e): 9, 
              (d, f): 14, (e, f): 10, (g, f): 2, (h, g): 1, 
              (g, i): 6, (h, i): 7}
    #This will run for every vertex in the graph
    for v in G.v:
        #Initialize adjacency lists for the graph
        G.adj[v] = []
    #For "u" and "v" in "weight", this will run
    for u, v in weight:
        #Add v to the adjacency list of u
        G.adj[u].append(v)
        #Add u to the adjacency list of v
        G.adj[v].append(u)
    #Find MST using Kruskal's algorithm
    kruskalEdges, kruskalWeight = mstKruskal(G, weight)
    #Indicates the question being answered
    print("Kruskal's Algorithm")
    #Outputs the edges found
    print(f"The MST found by Kruskal's algorithm is: A = {kruskalEdges}")
    #Outputs the weight found
    print(f"The total weight of the MST is: {kruskalWeight}\n")
    #Find MST using Prim's algorithm
    primEdges, primWeight = mstPrim(G, weight, a)
    #Indicates the question being answered
    print("Prim's Algorithm")
    #Outputs the edges found
    print(f"The MST found by Prim's algorithm is: A = {primEdges}")
    #Outputs the weight found
    print(f"The total weight of the MST is: {primWeight}")
#Runs the execute method
execute()