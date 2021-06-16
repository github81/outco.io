

"""

https://leetcode.com/problems/number-of-provinces/


-- pseudo code

Algorithm
	Create adjacency list from matrix
	DFS for unvisited nodes

DFS
	Housekeeping
		Set discovered[node] = current time
		Set lowLink[node] = current time
		Increment time
		Add to stack, onStack
	Iterate through the adjacency list
		If unvisited, do DFS on adjacent nodes.
		On backtrack, update lowlink (min(current, destination))
	If lowlink == discovered(current)
		Pop off nodes off stack until current node
		Increase countOfProvinces


-- java solution

class Solution {
    List<Integer>[] graph;
    int[] discovered;
    int[] lowLink;
    Deque<Integer> stack;
    boolean[] onStack;
    int count = 0;
    int time = 0;
    final int UNVISITED = -1;
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        discovered = new int[n];
        Arrays.fill(discovered, UNVISITED);
        lowLink = new int[n];
        Arrays.fill(lowLink, UNVISITED);
        stack = new ArrayDeque<>();
        onStack = new boolean[n];
        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j< n; j++) {
                if (i != j &&
                    isConnected[i][j] == 1) {
                    graph[i].add(j);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            if (discovered[i] == UNVISITED) {
                dfs(i);
            }
        }
        return count;
    }
    private void dfs(int current) {
        discovered[current] = time;
        lowLink[current] = time;
        time++;
        stack.push(current);
        onStack[current] = true;
        for (int destination : graph[current]) {
            if (discovered[destination] == UNVISITED) {
                dfs(destination);
            }
            if (onStack[destination]) {
                lowLink[current] = 
                    Math.min(lowLink[destination], 
                             lowLink[current]);
            }
        }
        if (discovered[current] == lowLink[current]) {
            for (int node = stack.pop(); ; node = stack.pop()) {
                onStack[node] = false;
                if (node == current) break;
            }
            count++;
        }
    }
}

"""