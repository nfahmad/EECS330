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
        #Related to the distance from one node to the other
        self.d = 0
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
#Both attributes (v.d and v.parent) will be first initialized
def initializeSingleSource(G, s):
    #This will run for every vertex in the graph
    for v in G.v:
        #Initialize distance for each vertex
        v.d = float("inf")
        #Initialize parent for each vertex
        v.parent = None
    #Initialize distance for source vertex
    s.d = 0
#This is used to iteratively update the two attributes of the vertices
def relax(u, v, w):
    #If a shorter path from u to v is found, this will run
    if v.d > u.d + w[(u, v)]:
        #Update the distance of v
        v.d = u.d + w[(u, v)]
        #Update the parent of v to be u
        v.parent = u
#After the algorithms are run, the SSSP solution can be constructed
def printPath(G, s, v):
    #If v is the source vertex, this will run
    if v == s:
        #Print the source vertex
        print(s, end="")
    #If the parent of the vertex is None, this will run
    elif v.parent == None:
        #Indicate that there is no path that exists
        print(f"no path from {s} to {v} exists ")
    #Otherwise, this will run
    else:
        #Print the path from "s" to "v.parent"
        printPath(G, s, v.parent)
        #Separate vertices by comma
        print(", ", end="")
    #This will run if the node is not the starting node
    if v != s:
        #Print the current vertex
        print(v, end="")
'''
The Bellman-Ford algorithm solves the general SSSP problem, 
where the edge weights may be negative and the graphs may contain cycles
'''
def bellmanFord(G, w, s):
    #Initialize v.d and v.parent for each vertex
    initializeSingleSource(G, s)
    #Sort edges by weight
    edges = sorted(w.keys(), key = lambda x : w[x])
    #This will run for every edge in the length of the Graph
    for i in range(1, len(G.v)):
        #This will run for every edge in the set of edges
        for edge in edges:
            #Unpack
            u, v = edge
            #Relax all edges repeatedly to find shortest-paths
            relax(u, v, w)
    #This will run for every edge in the set of edges
    for edge in edges:
        #Unpack
        u, v = edge
        #If the distance to vertex "v" can be reduced, this will run
        if v.d > u.d + w[(u, v)]:
            #Return False if there are negative-weight cycles in the graph
            return False
    #Return True if there are no negative-weight cycles in the graph
    return True
'''
Dijkstra's algorithm uses the priority queue similarly as how Prim's algorithm (for MST) uses the priority queue. 
Dijkstra's algorithm generalizes Breadth-First Search (BFS) by emanating “waves” from the source vertex to all other vertices
'''
def dijkstra(G, w, s):
    #Initialize v.d and v.parent for each vertex
    initializeSingleSource(G, s)
    #Create a priority queue
    Q = []
    #This will run for every vertex in the graph
    for u in G.v:
        #Initially, all the vertices are in priority queue "Q"
        heappush(Q, u)
    #Loop for Dijkstra's algorithm
    while Q:
        #Extract the vertex with the smallest distance from the priority queue "Q"
        u = heappop(Q)
        #Iterate through all vertices adjacent to vertex "u"
        for v in G.adj[u]:
            #Relax edges
            relax(u, v, w)
            #Update v.d and v.parent for all neighbors of u if possible
            heapify(Q)
#Creates a method that will use the different functions to print out their discoveries
def execute():
    #Assigns G to a graph
    G = Graph()
    #Create nodes for the graph
    s = Node("s")
    #Create nodes for the graph
    t = Node("t")
    #Create nodes for the graph
    x = Node("x")
    #Create nodes for the graph
    y = Node("y")
    #Create nodes for the graph
    z = Node("z")
    #Add the nodes to the list of vertices
    G.v = [s, t, x, y, z]
    #Assign weights to the edges
    weightBellmanFord = {(s, t): 6, (s, y): 7, (y, x): -3, (y, z): 9, (t, y): 8, (t, z): -4, (t, x): 5, (x, t): -2, (z, x): 7, (z, s): 2}
    #Assign weights to the edges
    weightDijkstra = {(s, t): 10, (s, y): 5, (y, x): 9, (y, z): 2, (y, t): 3, (t, y): 3, (t, x): 1, (x, z): 4, (z, x): 6, (z, s): 7}
    #This will run for every vertex in the graph
    for v in G.v:
        #Initialize adjacency lists for the graph
        G.adj[v] = []
    #For "u" and "v" in "weightBellmanFord", this will run
    for u, v in weightBellmanFord:
        #Add v to the adjacency list of u
        G.adj[u].append(v)
    #Run the Bellman-Ford algorithm
    bellmanFord(G, weightBellmanFord, s)
    #Indicates the question being answered
    print("1) Bellman-Ford Algorithm")
    #This will run for every vertex in the graph
    for v in G.v:
        #Outputs the shortest-path weight of the vertex
        print(f"   shortest-path weight of {v} to source vertex {s} = {v.d}")
        #Outputs the shortest-path
        print(f"   shortest-path from source vertex {s} to {v} =", end=" ")
        #Calls the printPath function
        printPath(G, s, v)
        #Adds a space
        print(" ")
        #Adds a space
        print(" ")
    #This will run for every vertex in the graph
    for v in G.v:
        #Initialize adjacency lists for the graph
        G.adj[v] = []
    #For "u" and "v" in "weightDijkstra", this will run
    for u, v in weightDijkstra:
        #Add v to the adjacency list of u
        G.adj[u].append(v)
    #Run Dijkstra's algorithm
    dijkstra(G, weightDijkstra, s)
    #Indicates the question being answered
    print("2) Dijkstra's Algorithm")
    #This will run for every vertex in the graph
    for v in G.v:
        #Outputs the shortest-path weight of the vertex
        print(f"   shortest-path weight of {v} to source vertex {s} = {v.d}")
        #Outputs the shortest-path
        print(f"   shortest-path from source vertex {s} to {v} =", end=" ")
        #Calls the printPath function
        printPath(G, s, v)
        #Adds a space
        print(" ")
        #Adds a space
        print(" ")
#Runs the execute method
execute()