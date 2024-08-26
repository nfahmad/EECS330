#Creates a global variable to reference something not in the list as NIL
NIL = "NIL"
#Creates a method that will use the different hashing functions to print out the sorted arrays
def execute():
    #Creates a variable for the size of the table
    exampleM = 13
    #Creates a variable for the first key we are searching for
    exampleKey1 = 14
    #Creates a variable for the second key we are searching for
    exampleKey2 = 66
    #Creates a table of the specified size
    exampleTable = [NIL] * exampleM
    #Inserts a value into the table
    hashInsert(exampleTable, 79, exampleM)
    #Inserts a value into the table
    hashInsert(exampleTable, 69, exampleM)
    #Inserts a value into the table
    hashInsert(exampleTable, 72, exampleM)
    #Inserts a value into the table
    hashInsert(exampleTable, 50, exampleM)
    #Inserts a value into the table
    hashInsert(exampleTable, 98, exampleM)
    #Inserts a value into the table
    hashInsert(exampleTable, 14, exampleM)
    #Indicates the test case that is being showcased
    print("Test Case 1")
    #Outputs the sorted table
    print(f"1) {exampleTable}")
    #Indicates if what was searched for is in the list
    print(f"2) The search for key {exampleKey1} returned index {hashSearch(exampleTable, exampleKey1, exampleM)}")
    #Indicates if what was searched for is in the list
    print(f"   The search for key {exampleKey2} returned index {hashSearch(exampleTable, exampleKey2, exampleM)}\n")
    #Creates a variable for the size of the table
    testCaseM = 7
    #Creates a variable for the first key we are searching for
    testCaseKey1 = 52
    #Creates a variable for the second key we are searching for
    testCaseKey2 = 11
    #Creates a table of the specified size
    testCaseTable = [NIL] * testCaseM
    #Inserts a value into the table
    hashInsert(testCaseTable, 10, testCaseM)
    #Inserts a value into the table
    hashInsert(testCaseTable, 82, testCaseM)
    #Inserts a value into the table
    hashInsert(testCaseTable, 40, testCaseM)
    #Inserts a value into the table
    hashInsert(testCaseTable, 35, testCaseM)
    #Inserts a value into the table
    hashInsert(testCaseTable, 15, testCaseM)
    #Inserts a value into the table
    hashInsert(testCaseTable, 21, testCaseM)
    #Inserts a value into the table
    hashInsert(testCaseTable, 52, testCaseM)
    #Indicates the test case that is being showcased
    print("Test Case 2")
    #Outputs the sorted table
    print(f"1) {testCaseTable}")
    #Indicates if what was searched for is in the list
    print(f"2) The search for key {testCaseKey1} returned index {hashSearch(testCaseTable, testCaseKey1, testCaseM)}")
    #Indicates if what was searched for is in the list
    print(f"   The search for key {testCaseKey2} returned index {hashSearch(testCaseTable, testCaseKey2, testCaseM)}")
#Double hashing uses the hash function h(k, i) = (h1(k) + i * h2(k)) mod m where h1(k) and h2(k) are auxiliary hash functions
def doubleHashing(key, probeNumber, tableSize):
    #This will run if the table size is 13
    if tableSize == 13:
        #h1 = key modulo table size
        h1 = key % tableSize
        #h2 = 1 + (key modulo number smaller than table size)
        h2 = 1 + (key % 11)
        #Using the hashing function, return the value
        return (h1 + probeNumber * h2) % tableSize
    #Otherwise, if the table size is 7, this will run
    elif tableSize == 7:
        #h1 = key modulo table size
        h1 = key % tableSize
        #h2 = 5 - (key modulo number smaller than table size)
        h2 = 5 - (key % 5)
        #Using the hashing function, return the value
        return (h1 + probeNumber * h2) % tableSize
'''
Creates a function to insert values into the hash table. Insert follows the probe sequence until an empty slot is found 
(for inserting the element) or realizing the table is full (can't insert)
'''
def hashInsert(inputTable, key, tableSize):
    #Begin the probe number at 0. For each key, the slots are probed using a probe sequence based on a hash function
    probeNumber = 0
    #Repeat the following lines until a condition is met
    while True:
        #Assigns a variable to the value returned through double hashing
        value = doubleHashing(key, probeNumber, tableSize)
        #If the value is not in the list, this will run
        if inputTable[value] == NIL:
            #Assigns the value to the key
            inputTable[value] = key
            #Returns the value
            return value
        #If the value is in the list, this will run
        else:
            #Increase the probe number
            probeNumber = probeNumber + 1
        #This will run if all positions have been probed
        if probeNumber == tableSize:
            #Breaks the loop
            break
'''
Creates a function to search for values in the hash table. Search follows the same probe sequence until success 
(the key is found) or failure (an empty slot is found or all positions are probed)
'''
def hashSearch(inputTable, key, tableSize):
    #Begin the probe number at 0. For each key, the slots are probed using a probe sequence based on a hash function
    probeNumber = 0
    #Repeat the following lines until a condition is met
    while True:
        #Assigns a variable to the value returned through double hashing
        value = doubleHashing(key, probeNumber, tableSize)
        #If the search is successful, this will run
        if inputTable[value] == key:
            #Return the found value
            return value
        #Increase the probe number
        probeNumber = probeNumber + 1
        #This will run if an empty slot is found or if all positions have been probed
        if inputTable[value] == NIL or probeNumber == tableSize:
            #Breaks the loop
            break
    #Indicate that the value being searched for is not in the list
    return NIL
#Runs the execute method
execute()