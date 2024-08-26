#Creates a method that will use the matrixMultiplyRecursive function to print out the final matrices
def execute():
    #This is the given matrix A in the lecture example
    exampleA = [[5, 2, 6, 1], [0, 6, 2, 0], [3, 8, 1, 4], [1, 8, 5, 6]]
    #This is a test case that contains a matrix of n >= 16
    testCaseA = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64],
    [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96],
    [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128],
    [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144],
    [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160],
    [161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176],
    [177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192],
    [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208],
    [209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224],
    [225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240],
    [241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256]]
    #This is the given matrix B in the lecture example
    exampleB = [[7, 5, 8, 0], [1, 8, 2, 6], [9, 4, 3, 8], [5, 3, 7, 9]]
    #This is a test case that contains a matrix of n >= 16
    testCaseB = [[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],
    [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64],
    [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48],
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2],
    [48, 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3],
    [64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4],
    [80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],
    [96, 90, 84, 78, 72, 66, 60, 54, 48, 42, 36, 30, 24, 18, 12, 6],
    [112, 105, 98, 91, 84, 77, 70, 63, 56, 49, 42, 35, 28, 21, 14, 7],
    [128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8],
    [144, 135, 126, 117, 108, 99, 90, 81, 72, 63, 54, 45, 36, 27, 18, 9],
    [160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],
    [176, 165, 154, 143, 132, 121, 110, 99, 88, 77, 66, 55, 44, 33, 22, 11]]
    #Creates an empty matrix of n >= 16
    exampleC = [[0 for _ in range(4)] for _ in range(4)]
    #Creates an empty matrix of n >= 16
    testCaseC = [[0 for _ in range(16)] for _ in range(16)]
    #This will print the matrix resulting from multiplying exampleA and exampleB
    print(f"1. {matrixMultiplyRecursive(exampleA, exampleB, exampleC, len(exampleC), 0, 0, 0)}")
    #This will print the matrix resulting from multiplying exampleA and exampleB
    print(f"2. {matrixMultiplyRecursive(testCaseA, testCaseB, testCaseC, len(testCaseC), 0, 0, 0)}")
#Creates a recursive method to multiply matrices
def matrixMultiplyRecursive(A, B, C, n, value1, value2, value3):
    #If the length of the matrix is equal to 1, this will run
    if n == 1:
        #Adjujsts the final matrix with new values
        C[value1][value2] += A[value1][value3] * B[value3][value2]
        #Returns the final matrix
        return C
    #Uses the length of the matrix for partitioning
    middle = n // 2
    #Uses recursion to divide and conquer
    matrixMultiplyRecursive(A, B, C, middle, value1, value2, value3)
    #Uses recursion to divide and conquer
    matrixMultiplyRecursive(A, B, C, middle, value1, value2, value3 + middle)
    #Uses recursion to divide and conquer
    matrixMultiplyRecursive(A, B, C, middle, value1, value2 + middle, value3)
    #Uses recursion to divide and conquer
    matrixMultiplyRecursive(A, B, C, middle, value1 + middle, value2, value3)
    #Uses recursion to divide and conquer
    matrixMultiplyRecursive(A, B, C, middle, value1, value2 + middle, value3 + middle)
    #Uses recursion to divide and conquer
    matrixMultiplyRecursive(A, B, C, middle, value1 + middle, value2 + middle, value3 + middle)
    #Uses recursion to divide and conquer
    matrixMultiplyRecursive(A, B, C, middle, value1 + middle, value2, value3 + middle)
    #Uses recursion to divide and conquer
    matrixMultiplyRecursive(A, B, C, middle, value1 + middle, value2 + middle, value3)
    #Returns the final matrix
    return C
#Runs the execute method
execute()
