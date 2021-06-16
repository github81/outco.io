
"""

https://github.com/OutcoSF/outco-class-98/blob/master/whiteboarding/w2_d1_dynamic_programming_2/222_consecutive_subarray_sum.md



222 - Consecutive Subarray Sum

Given an array of positive integers and a target value, 
return true if there is a subarray of consecutive elements 
that sum up to this target value.

Input: Array of integers, target value
Output: Boolean
Example

Input: [6,12,1,7,5,2,3], 14      	=>	Output: true (7+5+2)

l = 0
r = 0

l           r           r_target 
0           0           6
0           1           18
1           1           12
1           2           13
1           3           20
2           3           8
2           4           13
2           5           15
3           5           14            true          

Input: [8,3,7,9,10,1,13], 50		=>	Output: false
Constraints

Time Complexity: O(N)
Auxiliary Space Complexity: O(1)
All elements are positive


"""


