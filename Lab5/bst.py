#Makes a binary node class
class BinaryNode:
    #Initializes entry
    def __init__(self, entry):
        #Related to the entry held within the node
        self.entry = entry
        #Related to the child to the left of the node
        self.left = None
        #Related to the child to the right of the node
        self.right = None
'''
Inserts a new node into the tree by tracing a simple path down from the root based on the entry of the node 
and places it in an appropriate leaf position to maintain the binary-search-tree property
'''
def treeInsert(Tree, z):
    #Node being compared with "z"
    x = Tree
    #"y" will be parent of "z"
    y = None
    #Descend until reaching a leaf
    while x != None:
        #Adjust "y" to the current node
        y = x
        #If the value of the new node is less than the value of the current node, this will run
        if z.entry < x.entry:
            #Moves to the left child of the current node
            x = x.left
        #If the value of the new node is greater than the value of the current node, this will run
        else:
            #Moves to the right child of the current node
            x = x.right
    #Found the location, so insert "z" with parent "y"
    z.parent = y
    #If "y" is None, this will run
    if y == None:
        #The tree is empty
        Tree = z
    #If the new node value is less than the parent node value, this will run
    elif z.entry < y.entry:
        #Moves the new node to the left of the parent
        y.left = z
    #If the new node value is greater than the parent node value, this will run
    else:
        #Moves the new node to the right of the parent
        y.right = z
#Creates a method to walk through the tree in the order: left subtree -> node -> right subtree
def inOrderTreeWalk(x):
    #Creates a list to store the entry values
    entries = []
    #Creates a function to walk through the tree
    def treeWalk(node):
        #If the current node is not None, this will run
        if node != None:
            #Walk through left subtree
            treeWalk(node.left)
            #Append the entry of the current node into the list
            entries.append(str(node.entry))
            #Walk through the right subtree
            treeWalk(node.right)
    #Run the treeWalk method with the root as the current node
    treeWalk(x)
    #Print a sorted list
    print("1)", ", ".join(entries))
#Creates a method to find the nodes whose entries are the smallest
def treeMinimum(x):
    #While the left child of the current node is not none, this will run
    while x.left != None:
        #Moves the current node to the left child
        x = x.left
    #Return the node with the minimum entry value
    return x
#Creates a method to find the nodes whose entries are the largest
def treeMaximum(x):
    #While the right child of the current node is not none, this will run
    while x.right != None:
        #Moves the current node to the right child
        x = x.right
    #Return the node with the maximum entry value
    return x
#Creates a method to search for a key in the tree
def treeSearch(x, key):
    #If the current node is None, or if the key is equal to the entry value of the current node, this will run
    if x == None or key == x.entry:
        #Return the current node
        return x
    #If the key is less than the value of the entry value of the current node, this will run
    if key < x.entry:
        #Search the left subtree
        return treeSearch(x.left, key)
    #If the key is greater than the value of the entry value of the current node, this will run
    else:
        #Search the right subtree
        return treeSearch(x.right, key)
#Creates a method to find the successor of a node
def successor(x):
    #If the right child is none, this will run
    if x.right != None:
        #This will return the leftmost node in the right subtree
        return treeMinimum(x.right)
    #Otherwise, find the lowest ancestor of x whose left child is an ancestor of x
    else:
        #Assign the parent of the current node to "y"
        y = x.parent
        #Walk up the tree until a parent whose left child is the current node is reached
        while y != None and x == y.right:
            #Update the current node with its parent
            x = y
            #Update the parent with its parent
            y = y.parent
        #Return the parent node
        return y
#Creates a method to find the predecessor of a node
def predecessor(x):
    #If the left child is none, this will run
    if x.left != None:
        #This will return the rightmost node in the left subtree
        return treeMaximum(x.left)
    #Otherwise, find the lowest ancestor of x whose right child is an ancestor of x
    else:
        #Update the current node with its parent
        y = x.parent
        #Walk up the tree until a parent whose right child is the current node is reached
        while y != None and x == y.left:
            #Update the current node with its parent
            x = y
            #Update the parent with its parent
            y = y.parent
        #Return the parent node
        return y
#Creates a method that will use the different methods to print out the required outputs
def execute():
    #Creates the root of the tree and assigns it a value
    exampleRoot = BinaryNode(15)
    #Inserts a value into the tree
    treeInsert(exampleRoot, BinaryNode(6))
    #Inserts a value into the tree
    treeInsert(exampleRoot, BinaryNode(18))
    #Inserts a value into the tree
    treeInsert(exampleRoot, BinaryNode(3))
    #Inserts a value into the tree
    treeInsert(exampleRoot, BinaryNode(7))
    #Inserts a value into the tree
    treeInsert(exampleRoot, BinaryNode(17))
    #Inserts a value into the tree
    treeInsert(exampleRoot, BinaryNode(20))
    #Inserts a value into the tree
    treeInsert(exampleRoot, BinaryNode(2))
    #Inserts a value into the tree
    treeInsert(exampleRoot, BinaryNode(4))
    #Inserts a value into the tree
    treeInsert(exampleRoot, BinaryNode(13))
    #Inserts a value into the tree
    treeInsert(exampleRoot, BinaryNode(9))
    #Indicates the following outputs are for test case 1
    print("Test Case 1")
    #Passes the root into tree walk to output a sorted list of values
    inOrderTreeWalk(exampleRoot)
    #Outputs the minimum and maximum elements for the tree
    print(f"2) {treeMinimum(exampleRoot).entry} is the minimum element, {treeMaximum(exampleRoot).entry} is the maximum element")
    #Identifies the key to search for
    exampleKey = 13
    #Searches for the key
    exampleSearchResult = treeSearch(exampleRoot, exampleKey)
    #Outputs the successor of the key
    print(f"3) {successor(exampleSearchResult).entry}\n")
    #Creates the root of the tree and assigns it a value
    testCase2Root = BinaryNode(37)
    #Inserts a value into the tree
    treeInsert(testCase2Root, BinaryNode(24))
    #Inserts a value into the tree
    treeInsert(testCase2Root, BinaryNode(51))
    #Inserts a value into the tree
    treeInsert(testCase2Root, BinaryNode(7))
    #Inserts a value into the tree
    treeInsert(testCase2Root, BinaryNode(32))
    #Inserts a value into the tree
    treeInsert(testCase2Root, BinaryNode(41))
    #Inserts a value into the tree
    treeInsert(testCase2Root, BinaryNode(85))
    #Inserts a value into the tree
    treeInsert(testCase2Root, BinaryNode(2))
    #Inserts a value into the tree
    treeInsert(testCase2Root, BinaryNode(40))
    #Inserts a value into the tree
    treeInsert(testCase2Root, BinaryNode(120))
    #Indicates the following outputs are for test case 2
    print("Test Case 2")
    #Passes the root into tree walk to output a sorted list of values
    inOrderTreeWalk(testCase2Root)
    #Outputs the minimum and maximum elements for the tree
    print(f"2) {treeMinimum(testCase2Root).entry} is the minimum element, {treeMaximum(testCase2Root).entry} is the maximum element")
    #Identifies the key to search for
    testCase2Key = 40
    #Searches for the key
    testCase2SearchResult = treeSearch(testCase2Root, testCase2Key)
    #Outputs the predecessor of the key
    print(f"3) {predecessor(testCase2SearchResult).entry}")
#Runs the execute method
execute()
