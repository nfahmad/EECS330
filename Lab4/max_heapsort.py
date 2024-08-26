#Imports the math module
import math
#Creates a method that will use the heapSort function to print out the unsorted and sorted arrays
def execute():
    #This is the given array in the lecture example
    exampleArray = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    #This is a test case that contains 15 sorted numbers
    testCase = [22, 33, 55, 40, 67, 16, 38, 9, 11, 10, 34, 15, 75, 17, 26]
    #This will print exampleArray before sorting
    print(f"1. {exampleArray}")
    #This will pass exampleArray and its length into heapSort
    heapSort(exampleArray, len(exampleArray))
    #This will print exampleArray after sorting
    print(f"   {exampleArray}")
    #This will print testCase before sorting
    print(f"2. {testCase}")
    #This will pass testCase and its length into heapSort
    heapSort(testCase, len(testCase))
    #This will print testCase after sorting
    print(f"   {testCase}")
#This will create an algorithm that sorts an array using a max-heap
def heapSort(inputArray, size):
    #This will build the max-heap with the input array and its size
    buildMaxHeap(inputArray, size)
    #This will extract the elements one by one
    for value in range(size - 1, 0, -1):
        #Assigns exchange to inputArray[0]
        exchange = inputArray[0]
        #Assigns inputArray[0] to inputArray[value]
        inputArray[0] = inputArray[value]
        #Now the variables are swapped/exchanged so now the element is in a new location
        inputArray[value] = exchange
        #Discard the largest element from the heap
        size = size - 1
        #Restore the max-heap property
        maxHeapify(inputArray, 0, size)
#This will create/build a max-heap
def buildMaxHeap(inputArray, size):
    #This is the index of the last element in the array with a child
    value = math.floor(size / 2)
    #This will iterate over a range of values in decreasing order down to 0
    for value in range(value - 1, -1, -1):
        #This will call maxHeapify with the index of the last element in the array with a child
        maxHeapify(inputArray, value, size)
#This is a recursive procedure that maintains the max-heap property for heap "inputArray" on index "value"
def maxHeapify(inputArray, value, heapSize):
    #For an element with index value in the array, this is the index for the left child
    leftChild = 2 * value
    #For an element with index value in the array, this is the index for the right child
    rightChild = 2 * value + 1
    #If the index for the left child is less than the heap size
    #AND if the inputArray[leftChild] value is greater than the inputArray[value] value, this will run
    if leftChild < heapSize and inputArray[leftChild] > inputArray[value]:
        #Assigns the variable largest to the left child
        largest = leftChild
    #If the index for the left child is not less than the heap size
    #AND if the inputArray[leftChild] value is not greater than the inputArray[value] value, this will run
    else:
        #Assigns the variable largest to value
        largest = value
    #If the index for the right child is less than the heap size
    #AND if the inputArray[rightChild] value is greater than the inputArray[largest] value, this will run
    if rightChild < heapSize and inputArray[rightChild] > inputArray[largest]:
        #Assigns the variable largest to rightChild
        largest = rightChild
    #If largest is not equal to value, this will run
    if largest != value:
        #Assigns exchange to inputArray[value]
        exchange = inputArray[value]
        #Assigns inputArray[value] to inputArray[largest]
        inputArray[value] = inputArray[largest]
        #Now the variables are swapped/exchanged so now the element is in a new location
        inputArray[largest] = exchange
        #Recursively calls the maxHeapify to heapify the root
        maxHeapify(inputArray, largest, heapSize)
#Runs the execute method
execute()