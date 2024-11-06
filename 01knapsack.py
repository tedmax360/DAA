def knapsack_01(n, values, weights, W):
    dp = [[0] * (W+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    selected_items = []
    i, w = n, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
        i -= 1
    
    return dp[n][W], selected_items

if __name__ == "__main__":
    n = 3
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50

    max_value, selected_items = knapsack_01(n, values, weights, W)
    print("Maximum value:", max_value)
    print("Selected items:", selected_items)
    
    
    
    
    
    
    
    
    
    
    '''
    This code is solving the 0/1 Knapsack problem using dynamic programming. In this problem, given a set of items, 
    each with a value and a weight, and a knapsack with a fixed weight capacity, we need to determine the maximum 
    value that can be obtained by selecting a subset of items that fit within the weight capacity.
    
    Code Breakdown
1]knapsack_01(n, values, weights, W):

	This function implements the 0/1 Knapsack solution using dynamic programming.
	Parameters:
	 n: The number of items.
	 values: A list containing the values of the items.
	 weights: A list containing the weights of the items.
 	 W: The maximum weight capacity of the knapsack.
	Steps:
	 It initializes a 2D array dp of size (n+1) x (W+1) where dp[i][w] represents the maximum value 
	 that can be achieved using the first i items with a knapsack capacity of w.

	 For each item and weight combination, it updates the dp array based on the recurrence relation:
		If the weight of the current item is less than or equal to the current capacity w, the 
		item can be either included or excluded. The value is updated as: 
		dp[i][w]=max(dp[i−1][w],dp[i−1][w−weights[i−1]]+values[i−1])

		If the weight of the current item exceeds the capacity, it cannot be included, so we use: 
		dp[i][w]=dp[i−1][w]

		After filling the dp table, it traces back through the table to determine which items were 
		selected to achieve the maximum value. It adds the indices of the selected items to 
		the selected_items list.
2]Backtracking to find the selected items:
	Starting from the bottom-right corner of the dp table (dp[n][W]), the algorithm checks whether the 
	current item is included in the optimal solution:
		If dp[i][w] != dp[i-1][w], it means the item i-1 was included, so it is added to the selected_items 
		list, and the weight w is reduced by the item's weight.

	This process continues until the first row or column is reached.

3]Output: The function returns the maximum value (dp[n][W]) and the list of selected items (the indices of the 
	  items that are included in the optimal solution).
	  
example
n = 3
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

Here:
n = 3 means there are 3 items.
The values of the items are: [60, 100, 120].
The weights of the items are: [10, 20, 30].
The knapsack has a capacity of 50 units.

Backtracking for Selected Items
    Start from dp[3][50]:
        Since dp[3][50] != dp[2][50], Item 2 is included. Subtract its weight (30) 
        from 50, leaving a remaining capacity of 20.
        
    Then, dp[2][20] != dp[1][20], so Item 1 is also included. Subtract its weight (20) 
    from 20, leaving a remaining capacity of 0.
    
    Now, dp[1][0] is reached, and no more items are included.
    Selected Items: Item 1 (index 1) and Item 2 (index 2).
    
output:
    Maximum value: 220
    Selected items: [2, 1]
    
explanation:
The maximum value that can be obtained with the given capacity of 50 is 220.
The selected items are:
    Item 2 (with value 120 and weight 30),
    Item 1 (with value 100 and weight 20).
These items together fit within the knapsack's capacity of 50 and yield the maximum value of 220. 
The algorithm used dynamic programming to solve the problem efficiently.

complexity:
Time Complexity: O(n×W), where n is the number of items and W is the knapsack capacity.
Space Complexity: O(n×W), for storing the dp table.
    
    
    
    
    '''