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
#Uses the makeSet function to creates a new set with the variable
a = makeSet("a")
#Uses the makeSet function to creates a new set with the variable
b = makeSet("b")
#Uses the makeSet function to creates a new set with the variable
c = makeSet("c")
#Uses the makeSet function to creates a new set with the variable
d = makeSet("d")
#Uses the makeSet function to creates a new set with the variable
e = makeSet("e")
#Uses the makeSet function to creates a new set with the variable
f = makeSet("f")
#Uses the makeSet function to creates a new set with the variable
g = makeSet("g")
#Uses the makeSet function to creates a new set with the variable
h = makeSet("h")
#Merges the two sets
union(b,a)
#Merges the two sets
union(d,c)
#Merges the two sets
union(f,e)
#Merges the two sets
union(f,g)
#Merges the two sets
union(c,b)
#Merges the two sets
union(g,h)
#Merges the two sets
union(d,g)
#Returns the representative of the set containing the element
findSet(f)
#Indicates the following outputs are for the parent value of each element
print("Parent value of each element")
#Outputs the parent value of each element
print(f"a.p={a.parent.value}, b.p={b.parent.value}, c.p={c.parent.value}, d.p={d.parent.value}, e.p={e.parent.value}, f.p={f.parent.value}, g.p={g.parent.value}, h.p={h.parent.value}\n")
#Indicates the following outputs are for the rank value of each element
print("Rank value of each element")
#Outputs the rank value of each element
print(f"a.rank={a.rank}, b.rank={b.rank}, c.rank={c.rank}, d.rank={d.rank}, e.rank={e.rank}, f.rank={f.rank}, g.rank={g.rank}, h.rank={h.rank}")