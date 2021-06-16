

"""

https://github.com/OutcoSF/outco-class-98/blob/master/whiteboarding/w3_d1_matrix/A/310_rat_path.md



Tell Me a Time when you've failed.
Should take one minute; minute and a half at most

Prompt
Say: "Tell me a time when you've failed"

Do you hear these things?
Identify: Does the interviewee discuss their competencies based on what you have asked them? Competencies include:

Technical Skills (libraries, languages, etc.)
Interpersonal Skills
Prove: Does the interviewee provide a specific example (past experience or hypothetical scenario) to showcase competencies and/or fit? Is it presented in the form of a story (punchline, beginning, middle, positive end)?

Close: Does the interviewee showcase why the company should hire them and how their skills/experience/values will add value to and align with the team/company? Does the interviewee showcase what they have learned in "Prove" and how they will apply it to the new role?

310 - Rat Path
Given a maze, represented by a matrix of bits (values 0 and 1), 
a rat must find a path 
from index [0][0] to [n-1][m-1]. 
The rat can only travel to the right or down, 
and can only travel on 0 values. 
1 values represent walls.

Input:   maze (Matrix of elements with values either 0 or 1)
Output:  Array of two-item arrays indicating the path.
Example
Input:   [[0, 0, 0, 1],
          [0, 1, 0, 1],
          [0, 1, 0, 0],
          [0, 0, 1, 0]]

Output:  [[0, 0],
          [0, 1],
          [0, 2],
          [1, 2],
          [2, 2],
          [2, 3],
          [3, 3]]
Constraints
For M x N matrix.
Time Complexity: 0(MN)
Auxiliary Space Complexity: O(MN)
If not path found, return the following path: [[-1, -1]]
Remember, the rat can only move RIGHT or DOWN



Input:   [[0, 0, 0, 1],
          [0, 1, 0, 1],
          [0, 1, 0, 0],
          [0, 0, 1, 0]]

0,0 -> 0,1 -> 0,2 -> 1,2 ->

#edge cases
is the cell out of bounds, return False
is the value of cell 1, return False
is the cell the destination
    return True

#add to the output
add row,col to the Output

#traversal
a = traverse row+1, Col
b = traverse row, col+1


#backtracking


"""

