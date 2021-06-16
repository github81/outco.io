


"""


http://hr.gs/robot-paths
PW: Outc0SF

If you finish Robot Paths early,
try Matrix Spiral
http://hr.gs/matrix-spiral
PW: Outc0SF


# leet code questions
https://leetcode.com/problems/word-search/
https://leetcode.com/problems/word-search-ii/


"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'robotPaths' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


# time - O(3^mn) - 
# space - O(mn) - what is the longest possible path
def robotPaths(matrix):
    # Write your code here
    max_col = len(matrix[0])-1
    max_row = len(matrix)-1
    count = 0
    def traverse(row, col):
        
        nonlocal count
        
        #base cases
        if row < 0 or row > max_row or col < 0 or col > max_col:
            return
        if row == max_row and col == max_col:
            count += 1
            return
        if matrix[row][col] == 1:
            return
        
        #mark visited
        matrix[row][col] = 1
        
        #traverse
        traverse(row+1,col)
        traverse(row,col+1)
        traverse(row-1,col)
        traverse(row,col-1)
        
        #backtracking
        matrix[row][col] = 0
        
    
    traverse(0,0)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    matrix_rows = int(input().strip())
    matrix_columns = int(input().strip())

    matrix = []

    for _ in range(matrix_rows):
        matrix.append(list(map(int, input().rstrip().split())))

    result = robotPaths(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
