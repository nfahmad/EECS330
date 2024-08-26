#Creates a method that will use the insertionSort function to print out the sorted arrays
def execute():
    #This is the given array in the lecture example
    exampleArray = [5, 2, 4, 6, 1, 3]
    #This is a test case that contains 10 numbers
    testCase = [9, 1, 3, 2, 4, 7, 8, 5, 10, 6]
    #Uses an insertion-sort algorithm to sort exampleArray in order from least to greatest with a defined limit on sorting
    insertionSort(exampleArray, len(exampleArray))
    #This will print the sorted array and the question number
    print(f"1. {exampleArray}")
    #Uses an insertion-sort algorithm to sort testCase in order from least to greatest with a defined limit on sorting
    insertionSort(testCase, len(testCase))
    #This will print the sorted array and the question number
    print(f"2. {testCase}")
#Creates a method that will compare the array elements to each other and move each element to reach an array sorted from least to greatest
def insertionSort(inputArray, length):
    #This will run through every value in the defined range
    for value1 in range(1, length):
        #Assigns the current element to key
        key = inputArray[value1]
        #Assigns the predecessor of the index to value2
        value2 = value1 - 1
        #Creates a loop that will run until the end of the array is reached
        while value2 >= 0 and inputArray[value2] > key:
            #The array is appended with a new predecessor of the index
            inputArray[value2 + 1] = inputArray[value2]
            #Moves the predecessor to a new value
            value2 = value2 - 1
        #A new current element is assigned
        inputArray[value2 + 1] = key
    #This will return the sorted array
    return inputArray
#Runs the execute method
execute()