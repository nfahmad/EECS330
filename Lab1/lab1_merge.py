#Creates a method that will use the mergeSort function to print out the sorted arrays
def execute():
    #This is the given array in the lecture example
    exampleArray = [6, 5, 12, 10, 9, 1]
    #This is a test case that contains 16 numbers
    testCase = [10, 14, 9, 16, 1, 6, 12, 5, 11, 15, 2, 3, 7, 13, 4, 8]
    #Uses a merge-sort algorithm to sort exampleArray in order from least to greatest
    mergeSort(exampleArray)
    #This will print the sorted array and the question number
    print(f"1. {exampleArray}")
    #Uses a merge-sort algorithm to sort testCase in order from least to greatest
    mergeSort(testCase)
    #This will print the sorted array and the question number
    print(f"2. {testCase}")
#Creates a method that will split the inputArray into two subarrays and sort through them
def mergeSort(inputArray):
    #This makes sure the recursion depth is not exceeded
    if len(inputArray) > 1:
        #This divides the inputArray into two subarrays
        middle = len(inputArray)//2
        #This defines the leftArray as everything to the left of the middle point
        leftArray = inputArray[:middle]
        #This defines the rightArray as everything to the right of the middle point
        rightArray = inputArray[middle:]
        #Sorts the left half through recursion
        mergeSort(leftArray)
        #Sorts the right half through recursion
        mergeSort(rightArray)
        #Creates the initial index for the first subarray
        value1 = 0
        #Creates the initial index for the second subarray
        value2 = 0
        #Creates the initial index for the final subarray
        value3 = 0
        #This creates a loop that will run until the end of either the left array or the right array are reached
        while value1 < len(leftArray) and value2 < len(rightArray):
            #Determines if the current index on the left array is less than the current index on the right array
            if leftArray[value1] < rightArray[value2]:
                #If the case is true, the final subarray is appended with the new value
                inputArray[value3] = leftArray[value1]
                #Moves the index forward
                value1 += 1
            #If the current index on the left array is not less than the current index on the right array
            else:
                #The case is not true and therefore the final subarray is appended with the new value
                inputArray[value3] = rightArray[value2]
                #Moves the index forward
                value2 += 1
            #Moves the index forward
            value3 += 1
        #Creates a loop to run when there are no more elements in the left array
        while value1 < len(leftArray):
            #The final subbaray is appended with the new value
            inputArray[value3] = leftArray[value1]
            #Moves the index forward
            value1 += 1
            #Moves the index forward
            value3 += 1
        #Creates a loop to run when there are no more elements in the right array
        while value2 < len(rightArray):
            #The final subbaray is appended with the new value
            inputArray[value3] = rightArray[value2]
            #Moves the index forward
            value2 += 1
            #Moves the index forward
            value3 += 1
#Runs the execute method
#execute()
            

array = [9,2,7,11,36,20,5,16,4,12]
#start = 0
#end = (len(array) - 1)

mergeSort(array)

#print(array)