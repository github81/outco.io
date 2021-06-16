
import os

"""

http://hr.gs/binary-tree
PW: Outc0SF


Example Tree:
               4
             /   \
           2       5
         /   \       \
       1       3       7
                     /   \
                   6      8


1.	BFS
2.	Pre-order DFS
3.	In-order DFS
4.	Post-order DFS
5.	Serialized binary trees

"""


#	[4,2,5,1,3,7,6,8]
# use cases:
#	[[4],[2,5],[1,3,7],[6,8]]
#	[[4,[4]] , [2,[4,2]] 
def treeBFS(root):
	
	bfs = []
	result = []
	if not root:
		return result
	
	bfs.append(root)
	while bfs:
		
		node = bfs.pop(0)
		result.append(node.value)		
		
		if node.left:
			bfs.append(node.left)
		if node.right:
			bfs.append(node.right)
		
	return result
	
	
	
"""
               4
             /   \
           2       5
         /   \       \
       1       3       7
                     /   \
                   6      8

4,2,1,3,5,7,6,8
"""

#iteration and recursion
def preDFS(root):
	# Write your code here
    result = []
    def traverse(curr):
        if not curr:
            return
        result.append(curr.value)
        traverse(curr.left)
        traverse(curr.right)

    traverse(root)
    return result

def preDFSIteration(root):
	pass




"""
               4
             /   \
           2       5
         /   \       \
       1       3       7
                     /   \
                   6      8

1,2,3,4,5,6,7,8
"""
#iteration and recursion
def inDFS(root):
	pass



"""
               4
             /   \
           2       5
         /   \       \
       1       3       7
                     /   \
                   6      8

1,3,2,6,8,7,5,4
"""

#iteration and recursion
def postDFS(root):
	pass


# generate tree from list
def deserialize(lst):
    if len(lst) == 0:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not -1:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        if i + 1 < len(lst) and lst[i + 1] is not -1:
            current.right = TreeNode(lst[i + 1])
            queue.append(current.right)
        i += 2
    return root

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    compressed_tree_count = int(input().strip())

    compressed_tree = []

    for _ in range(compressed_tree_count):
        compressed_tree_item = int(input().strip())
        compressed_tree.append(compressed_tree_item)
        
    root = deserialize(compressed_tree)

    result = treeBFS(root)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
