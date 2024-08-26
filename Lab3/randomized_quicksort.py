#Imports the random module to make random numbers
import random
#Creates a method that will use the randomizedQuicksort function to print out the sorted arrays
def execute():
    #This is the given array in the lecture example
    exampleArray = [2, 1, 7, 8, 3, 5, 6, 4]
    #This will start the index at 0 for the array sorting
    exampleStart = 0
    #This will define the limit on sorting
    exampleEnd = (len(exampleArray) - 1)
    #Uses a randomized quicksort algorithm to sort exampleArray in order
    randomizedQuicksort(exampleArray, exampleStart, exampleEnd)
    #This will print the sorted array and the question number
    print(f"1. {exampleArray}")
    #This is a test case that contains 15 numbers
    testCase = [22, 33, 55, 40, 67, 16, 38, 9, 11, 10, 34, 15, 75, 17, 26]
    #This will start the index at 0 for the array sorting
    testStart = 0
    #This will define the limit on sorting
    testEnd = (len(testCase) - 1)
    #Uses a randomized quicksort algorithm to sort testCase in order
    randomizedQuicksort(testCase, testStart, testEnd)
    #This will print the sorted array and the question number
    print(f"2. {testCase}")
#Creates a method to select the pivot and rearrange the array elements between the two sides of the partition
def partition(inputArray, startIndex, endIndex):
    #This is the pivot
    x = inputArray[endIndex]
    #The highest index into the low side
    value1 = startIndex - 1
    #Assign value2 to startIndex
    value2 = startIndex
    #Process each element other than the pivot
    for value2 in range(startIndex, endIndex):
        #Determines if the element belongs on the low side
        if inputArray[value2] <= x:
            #Index of a new slot in the low side
            value1 = value1 + 1
            #Assigns exchange to inputArray[value1]
            exchange = inputArray[value1]
            #Assigns inputArray[value1] to inputArray[value2]
            inputArray[value1] = inputArray[value2]
            #Now the variables are swapped/exchanged so now the element is in a new location
            inputArray[value2] = exchange
    #Assigns exchange to inputArray[value1 + 1]
    exchange = inputArray[value1 + 1]
    #Assigns inputArray[value1 + 1] to inputArray[endIndex]
    inputArray[value1 + 1] = inputArray[endIndex]
    #Now the variables are swapped/exchanged so now the pivot goes just to the right of the low side
    inputArray[endIndex] = exchange
    #Returns the new index of the pivot
    return value1 + 1
#Creates a method to randomly picks an element of the array as the pivot
def randomizedPartition(inputArray, startIndex, endIndex):
    #This will return a random number between the given range
    value1 = random.randint(startIndex, endIndex)
    #Assigns exchange to inputArray[endIndex]
    exchange = inputArray[endIndex]
    #Assigns inputArray[endIndex] to inputArray[value1]
    inputArray[endIndex] = inputArray[value1]
    #Now the variables are swapped/exchanged so now there is a new pivot
    inputArray[value1] = exchange
    #This will return the value of the new index of the pivot
    return partition(inputArray, startIndex, endIndex)
#Creates a method to partition and then recurse using the index returned by partition to return a sorted array
def randomizedQuicksort(inputArray, startIndex, endIndex):
    #If the starting index value is less than the ending index value, this will run
    if startIndex < endIndex:
        #Calls the randomizedPartition function and assigns it to partitionIndex
        partitionIndex = randomizedPartition(inputArray, startIndex, endIndex)
        #Recursively calls the randomizedQuicksort to separately sort the elements before and after partition
        randomizedQuicksort(inputArray, startIndex, partitionIndex - 1)
        #Recursively calls the randomizedQuicksort to separately sort the elements before and after partition
        randomizedQuicksort(inputArray, partitionIndex + 1, endIndex)
    #This will return the sorted array
    return inputArray

def quicksort(inputArray, startIndex, endIndex):
    if startIndex < endIndex:
        partitionIndex = partition(inputArray, startIndex, endIndex)
        print(inputArray)
        quicksort(inputArray, startIndex, partitionIndex - 1)
        quicksort(inputArray, partitionIndex + 1, endIndex)
    return inputArray

#Runs the execute method
#execute()


array = [9,2,7,11,36,20,5,16,4,12]
start = 0
end = (len(array) - 1)

print(quicksort(array, start, end))



