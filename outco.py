
#
# word puzzle - recursion
#

def gridWord():
	pass


#
# Complete the 'latticePaths' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER n
#

def latticePaths(m,n,res={}):
    
    if m < 0 or n < 0:
        return 0
    
    if m == 0 and n == 0:
        return 1
    
    if (m,n) in res:
        return res[(m,n)]
        
    res[(m-1,n)] = latticePaths(m-1,n)
    res[(m,n-1)] = latticePaths(m,n-1)
    
    return res[(m-1,n)] + res[(m,n-1)]



"""
function powerset(word) {
    let output = [];
    function recurse(index, buildStr) {
        // Base case --> index is at length of word
        if(index == word.length) {
            output.push(buildStr);
            return;
        }
        // Recursive Relations
        // Either add the char, or skip it. Either way increment indwex
        recurse(index+1, buildStr + word[index]);
        recurse(index+1, buildStr);
    }
    recurse(0,"");
    return output;
}
"""        
def powerSet(word):
	pass
	
	
	
"""

230 - Non-Consecutive Ones

Given a positive integer n, return an array of all the binary strings of length n that DO NOT contain consecutive 1s.

Input: n (Integer)
Output: [Str] (Array of Strings)
Example

Input: 2
Output: ["00", "01", "10"]

Input: 3
Output: ["000", "001", "010", "100", "101"]
Constraints

Time Complexity: O(2^N)
Auxiliary Space Complexity: O(2^N)
The order of the strings in the array does not matter.

Use recursion to solve this problem.

Solution

Key Insight:

Use helper method recursion, similar to how you would generate all the bit strings of a given length, but only recurse with a 1 if there isn't a 1 at the preceding index.

Initialize an empty array and return it at the end of the function
Initialize a helper method that takes a string, substr, as an input, and it invoked below with the empty string
a) If the length of substr is equal to n, push substr into the result array and return
b) Otherwise, invoke the helper function again with substr + 0 as its argument
c) If the character at the last index of substr is a 0, then recurse with substr + 1
Code

function NonConsecutiveOnes(n) {
  let result = [];

  function recurse(substr) {
    if(substr.length === n) {
      result.push(substr);
      return;
    }
    recurse(substr + 0);
    if(substr[substr.length - 1] !== "1") {
      recurse(substr + 1)
    }
  }

  recurse("");
  return result;
}


console.log(NonConsecutiveOnes(4));


"""
	
def nonConsecutiveOnes(n):
	pass
	
	
	
"""

231 - Capital Permutations

Given a string str of lowercase alphabetical characters, return the set of all permutations of those characters in upper AND lowercase.

Advanced

Solve the same problem, except now you may have number characters in your string (which don't have a lowercase or uppercase, but should still be included in your result) and capital letters, that need to be lowercased.

Input: str (String)
Output: [Str] (Array of Strings)
Example

Input: "abc"
Output: ["ABC", "ABc", "AbC", "aBC", "Abc", "aBc", "abC", "abc"]


Advanced:

Input: "A1d3"
Output: ["A1D3", "a1D3", "A1d3", "a1d3"]
Constraints

Time Complexity: O(2^N)
Space Complexity: O(2^N)
The order of the strings in the final result does not matter.

In the basic solution, all the input characters will be lowercase letters.

In the advanced solution, the input characters can be uppercase letters and numbers too.

Resources

Capital Permutations on Leetcode;

Solution

Use helper method recursion to solve this problem, keeping track of the depth and the permutation you are building up.

Basic

Instantiate a result array, and return it at the end.
Declare a recursive helper function called permute that takes two arguments substr and depth, and invoke this function with an empty string and 0.
The base case when depth is equal to the lenght of the input str, push whatever substr you've built up so far into result and return.
The recursive cases to handle are
Advanced

Here you need to manage three scenarios in your recursion.

If you the character you are looking at is a number, perform a single recursive call with that number concatenated to substr and depth + 1;
If the character you are looking at is a capital, perform two recursive calls:
a) One with substr and that character, with depth + 1.
b) The other with substr and the lowercase version of that character, with depth + 1.
If the character you are looking at is lowercase, just do what you did in the basic solution.
a) Recurse with substr and that character, with depth + 1.
b) Recurse with substr and that character uppercased, with depth + 1
Code

function captialPermutationsBasic(str) {  //Given a string of letters in lowercase
  let result = [];

  function permute(substr, depth) {
    if(depth === str.length) {
      result.push(substr);
      return;
    }
    permute(substr + str[depth], depth + 1);
    permute(substr + str[depth].toUpperCase(), depth + 1);
  }

  permute("", 0);

  return result;
}

console.log(capitalPermutationsBasic("abc"));

function capitalPermutationsAdvanced(S) { //Given a string of letters containing uppercase, lowercase and numbers
    let result = [];

    function recurse(substr, depth) {
        if(depth === S.length) {
            result.push(substr);
            return;
        }
        if(!isNaN(S[depth])) {
            recurse(substr + S[depth], depth + 1)
        } else if(S[depth] == S[depth].toUpperCase()) {
            recurse(substr + S[depth].toLowerCase(), depth + 1);
            recurse(substr + S[depth], depth + 1);
        } else {
            recurse(substr + S[depth].toUpperCase(), depth + 1);
            recurse(substr + S[depth], depth + 1);
        }
    }
    recurse("", 0)
    return result;
};

console.log(capitalPermutationsAdvanced("A1bC2"));


"""

def capitalPermutations(s):
	pass
	

#########################################################################################
###### 		DYNAMIC PROGRAMMING		#####################################################
#########################################################################################



	
	 		

	
	
	
	
"""

https://github.com/OutcoSF/outco-class-98/tree/master/whiteboarding/w1_d4_dynamic_programming_1/A

let calls = 0;

function lps(str) {
  let cache = {};
  function checkSubstring(i, j) {
    calls++;
    let key = i + '_' + j;
    if (key in cache) {
      return cache[key];
    }
    if (i === j) {
      return 1;
    }
    if (i === j - 1) {
      if (str[i] === str[j]) {
        return 2;
      }
      return 1;
    }

    if (str[i] === str[j]) {
      let result = checkSubstring(i + 1, j - 1) + 2;
      cache[key] = result;
      return result;
    } else {
      let left = checkSubstring(i + 1, j);
      let right = checkSubstring(i, j-1);
      let result = Math.max(left, right);
      cache[key] = result;
      return result;
    }
  }

  return checkSubstring(0, str.length - 1);
}



function lpsTab(str) {
  let matrix = new Array(str.length);
  for (let i = 0; i < str.length; i++) {
    matrix[i] = new Array(str.length).fill(0);
  }

  for (let i = 0; i < str.length; i++) {
    matrix[i][i] = 1;
  }


  for (let i = 0; i < str.length - 1; i++) {
    if (str[i] === str[i + 1]) {
      matrix[i][i+1] = 2;
    } else {
      matrix[i][i+1] = 1;
    }
  }



  for (let i = str.length - 3; i > -1; i--) {
    for (let j = i + 2; j < str.length; j++) {
      if (str[i] === str[j]) {
        matrix[i][j] = matrix[i+1][j-1] + 2;
      } else {
        matrix[i][j] = Math.max(matrix[i+1][j], matrix[i][j-1]); 
      }
    }
  }

  printMatrix(matrix);
  return matrix[0][str.length - 1];

}

function printMatrix(matrix) {
  for (let row of matrix) {
    console.log(JSON.stringify(row));
  }
}


// console.log(lpsTab("ttbtctcbt"));
console.log(lpsTab("vvtvv"));


"""
def longestPalindrome():
	pass
	
if __name__=="__main__":
	pass