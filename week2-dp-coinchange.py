
# subtract and remove method
# #1 =>	recursion
# #2 => recursion with memoization
# #3 => tabulation
"""

let calls = 0;

function coinChange(coinsInput, target) {
  const cache = {};
  function findWays(total, coins) {
    calls++;
    let key = total + '_' + coins.length;
    if (key in cache) {
      return cache[key];
    }
    if (total === 0 && coins.length === 0) {
      return 1;
    }
    if (total < 0) {
      return 0;
    }
    if (total > 0 && coins.length === 0) {
      return 0;
    }

    let left = findWays(total - coins[coins.length - 1], coins);
    let popped = coins.pop();
    let right = findWays(total, coins);
    coins.push(popped);

    cache[key] = left + right;
    return left + right;
  }

  return findWays(target, coinsInput);
}

// console.log(coinChange([1,2,4], 50));
// console.log("CALLS: ", calls);


function coinChangeTab(coins, target) {
  let table = new Array(target + 1).fill(0);
  table[0] = 1;

  console.log("TABLE: ", table);
  for (let coin of coins) {
    for (let i = coin; i < table.length; i++) {
      table[i] = table[i] + table[i - coin];
    }
    console.log("TABLE: ", table);
  }


  return table[target];
}

console.log(coinChangeTab([1,2,4], 5));

"""

def coinsChange(coinsInput,target):
	
	cache = {}
	calls = 0
	
	def findWays(total, coins):
	
		nonlocal calls
	
		key = str(total) + "_" + str(len(coins))
		calls += 1	
		if total == 0 and len(coins) == 0:
			return 1
			
		if total < 0:
			return 0
			
		if total > 0 and len(coins) == 0:
			return 0
			
		if key in cache:
			return cache[key]
			
		left = findWays(total - coins[len(coins)-1],coins)
		popped = coins.pop()
		right = findWays(total,coins)
		
		cache[key] = left + right
		
		coins.append(popped)
		
		return cache[key]
		
	numWays = findWays(target,coinsInput)
	print(calls)
	return numWays


if __name__ == "__main__":
	coinsInput = [1,2,4]
	target = 5

	#coinsInput = [1]
	#target = 1

	print(coinsChange(coinsInput,target))