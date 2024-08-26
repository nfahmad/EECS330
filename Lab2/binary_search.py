#Imports the math module
import math
#Creates a method that will use the recursiveBinarySearch function to print out the indices
def execute():
    #This is the given array in the lecture example
    exampleArray = [3, 5, 7, 8, 9, 12, 15]
    #This is a test case that contains 10 sorted numbers
    testCase = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #This will print the index for what is being searched and the question number
    print(f"1. {recursiveBinarySearch(exampleArray, 9, 0, len(exampleArray) - 1)}")
    #This will print the array, the index for what is being searched, and the question number
    print(f"2. {testCase}, {recursiveBinarySearch(testCase, 9, 0, len(testCase) - 1)}")
#Creates a recursive method to search for the key in a sorted array between indices low and high
def recursiveBinarySearch(inputArray, key, low, high):
    #If the low value is greater than the high value, this will run
    if low > high:
        #Indicates to the user that the array is not sorted
        print("This array is not sorted")
    #Assigns "middle" as the largest integer less than or equal to the result of the division
    middle = math.floor((low + high)/2)
    #If what is being searched is in the index middle of the input array, this will run
    if key == inputArray[middle]:
        #Returns the array index found for the searched element
        return middle
    #If what is being searched is greater than the index middle of the input array, this will run
    elif key > inputArray[middle]:
        #Uses recursion to increase the lower index to continue searching
        return recursiveBinarySearch(inputArray, key, middle + 1, high)
    else:
        #Uses recursion to decrease the higher index to continue searching
        return recursiveBinarySearch(inputArray, key, low, middle - 1)
#Runs the execute method
execute()