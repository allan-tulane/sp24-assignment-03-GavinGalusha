# CMPS 2200 Assignment 3
## Answers

**Name:**______Gavin Galusha___________________


Place all written answers from `assignment-03.md` here for easier grading.

1a) 
To make N dollars using the fewest number of coins in powers of 2 (2^0, 2^1, ..., 2^k), begin with the largest coin denomination that does not exceed N. Subtract this coin's value from N to get a new N. Repeat this process until N equals zero.

1b) 
The optimal greedy choice for any N is to select 2^k where k is the highest integer such that 2^k <= N. This choice is ideal as it reduces N by the largest amount in a single step, creating a smaller, independent problem: making change for N - 2^k. This subproblem is solved with the same greedy strategy. The denominations' binary nature ensures no better solution exists that uses smaller coins for 2^k since more coins would be required.

1c)  The work and span of this approach are O(log N) because of the logarithmic number of coin types.

2a) Imagine you need 4$ in change and want minimum amount of coines, and you have coins of value 1, 2, and 4. A greedy algorithm might pick 2 2$, whereas an optimal strategy would be to just take the 4$ coin.

2b) The optimal change to create for an amount N stems from the optimal solutions to the sub-problems for less than N amounts. If you know all minimum coin amounts required for all amounts less than N, then the optimal amount for N can be determined by adding one coin to the minimum of the optimal solutions for N-D_i for each denomination D_i that is available.

2c) Topdown memoization uses recursion to solve the problem, and saves results from subproblems to improve efficiency and prevent uneeded repetition


def CoinChangeRecursive(N, denominations):
	memo = [-1] * (N + 1)
	memo[0] = 0

	def FindMinCoins(amount):
		if memo[amount] >= 0:
				return memo[amount]

		minCoins = float('inf')
		for coin in denominations:
				if coin <= amount:
						candidate = FindMinCoins(amount - coin) + 1
						minCoins = min(minCoins, candidate)

		memo[amount] = minCoins
		return minCoins

	result = FindMinCoins(N)
	return "Change cannot be made with the given denominations" if 		result == float('inf') else result

work = O(Nk)
Span = O(N)