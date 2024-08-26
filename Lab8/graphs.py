#Makes a graph class
class Graph:
    #Initializes the graph object
    def __init__(self):
        #This creates a dictionary to store vertex objects
        self.v = dict()
        #This creates a dictionary to store adjacency lists
        self.adj = dict()
#Makes a breadth-first class
class BreadthFirst:
    #Initializes the breadth-first object
    def __init__(self):
        #Assigns the color
        self.color = "white"
        #Distance from the source to the vertex
        self.d = -1
        #Predecessor of vertex
        self.pi = None
#Makes a depth-first class
class DepthFirst:
    #Initializes the depth-first object
    def __init__(self):
        #Assigns the color
        self.color = "white"
        #First discovery time of vertex (1st timestamp)
        self.d = 0
        #Finishing time of vertex (2nd timestamp)
        self.f = 0
        #Predecessor of vertex
        self.pi = None
'''
Systematically explores the edges of G to discover every vertex that is reachable from source.
Computes the distance of source vertex to every vertex in the graph, where the distance means
the smallest number of edges needed to go from source vertex to vertex.
'''
def bfs(G, source):
    #This is a set of the vertices
    vertices = {"r", "s", "t", "u", "v", "w", "x", "y", "z"}
    #This is a set of the edges
    edges = {("r", "s"), ("s", "u"), ("s", "v"), ("t", "u"),
             ("r", "t"), ("u", "y"), ("v", "y"), ("r", "w"),
             ("v", "w"), ("w", "z"), ("x", "y"), ("x", "z"), ("w", "x")}
    #This will run for every node in the set of vertices
    for node in vertices:
        #Initializes vertices
        G.v[node] = BreadthFirst()
        #Initializes adjacency lists
        G.adj[node] = []
    #This will run for every edge in the set of edges
    for edge in edges:
        #Unpack
        u, v = edge
        #Add v to the adjacency list of u
        G.adj[u].append(v)
        #Add u to the adjacency list of v
        G.adj[v].append(u)
        #Sorts the list
        G.adj[u].sort()
        #Sorts the list
        G.adj[v].sort()
    #Create an empty queue
    queue = []
    #Source vertex is discovered for the first time
    G.v[source].color = "gray"
    #Source vertex has a distance of 0
    G.v[source].d = 0
    #Append source to the queue (enqueue)
    queue.append(source)
    #Perform BFS
    while queue:
        #Remove a vertex from the queue (dequeue)
        uVar = queue.pop(0)
        #Assigns u to the object associated to the vertex
        u = G.v[uVar]
        #Search the neighbors of u
        for vVar in G.adj[uVar]:
            #Assigns v to the object associated to the vertex
            v = G.v[vVar]
            #Is v being discovered now?
            if v.color == "white":
                #Vertex is discovered for the first time
                v.color = "gray"
                #Update the distance to the source
                v.d = u.d + 1
                #Assign the predecessor to u
                v.pi = u
                #v is now on the frontier
                queue.append(vVar)
                #Outputs the vertex discovered, and its distance to the source
                print(f"   {vVar} is discovered, it has a distance of {v.d} to the source {source}")
        #u is now behind the frontier
        u.color = "black"
'''
Starts from any vertex, and searches “deeper” in the graph whenever possible,
before backtracking to search for other vertices in the frontier
'''
def dfs(G):
    #This is a list of the vertices
    vertices = ["u", "v", "y", "x", "w", "z"]
    #This is a set of the edges
    edges = {("u", "v"), ("u", "x"), ("x", "v"), ("v", "y"),
             ("y", "x"), ("w", "y"), ("w", "z"), ("z", "z")}
    #This will run for every node in the set of vertices
    for node in vertices:
        #Initializes vertices
        G.v[node] = DepthFirst()
        #Initializes adjacency lists
        G.adj[node] = []
    #This will run for every edge in the set of edges
    for edge in edges:
        #Unpack
        u, v = edge
        #Add v to the adjacency list of u
        G.adj[u].append(v)
        #Add u to the adjacency list of v
        G.adj[v].append(u)
        #Sorts the list
        G.adj[u].sort()
        #Sorts the list
        G.adj[v].sort()
    #This will run for every u in the set of vertices
    for u in vertices:
        #All vertices start as undiscovered
        G.v[u].color = "white"
        #All vertices start with their predecessors as NIL
        G.v[u].pi = None
    #Allows for modification of time outside of the current scope
    global time
    #Time starts at 0
    time = 0
    #Perform DFS
    for u in vertices:
        #If the vertex is undiscovered, this will run
        if G.v[u].color == "white":
            #Runs the dfsVisit function starting at vertex u
            dfsVisit(G, u)
    #For every u in vertices
    for u in vertices:
        #Output the vertex with its discovery and finishing times
        print(f"   {u} is discovered at time {G.v[u].d}, it finished at time {G.v[u].f}")
#This function assists with searching for unexplored vertices
def dfsVisit(G, u):
    #Assigns uVar to the object associated to the vertex
    uVar = G.v[u]
    #Allows for modification of time outside of the current scope
    global time
    #White vertex u has just been discovered
    time = time + 1
    #Set the discovery time for the vertex
    uVar.d = time
    #The vertex is discovered for the first time
    uVar.color = "gray"
    #Explore each edge (u,v)
    for v in G.adj[u]:
        #Assigns vVar to the object associated to the adjacent vertex
        vVar = G.v[v]
        #If the vertex is undiscovered, this will run
        if vVar.color == "white":
            #Set the predecessor to the current vertex
            vVar.pi = uVar
            #Recursively visit the adjacent vertex
            dfsVisit(G, v)
    #Increase the time after visiting all vertices
    time = time + 1
    #Set the finishing time for the vertex
    uVar.f = time
    #Blacken u; it is finished
    uVar.color = "black"
#Creates a method that will use the different functions to print out the correct order of discoveries
def execute():
    #Assigns bfsGraph to a graph
    bfsGraph = Graph()
    #Indicates the question being answered
    print("1) Breadth-first search (BFS)")
    #Indicates that vertex s is the source and therefore the first vertex that is discovered
    print(f"   s is discovered, it has a distance of 0 to the source s")
    #Runs the bfs function using bfsGraph and the source s
    bfs(bfsGraph, "s")
    #Prints a blank line for separation
    print(" ")
    #Indicates the question being answered
    print("2) Depth-first search (DFS)")
    #Assigns dfsGraph to a graph
    dfsGraph = Graph()
    #Runs the dfs function using dfsGraph
    dfs(dfsGraph)
#Runs the execute method
execute()