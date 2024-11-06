class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(w, arr):
    arr.sort(key=lambda x: x.profit/x.weight, reverse=True)
    finalValue = 0.0
    for item in arr:
        if w >= item.weight:
            finalValue += item.profit
            w -= item.weight
        else:
            finalValue += item.profit * (w/item.weight)
            break
    return finalValue

if __name__ == "__main__":
    n = int(input("Enter number of items-\n"))
    arr = []
    for i in range(n):
        profit = int(input("Enter profit of item " + str(i + 1) + "-\n"))
        weight = int(input("Enter weight of item " + str(i + 1) + "-\n"))
        arr.append(Item(profit, weight))
    w = int(input("Enter capacity of knapsack-\n"))
    print("Maximum value in knapsack: ", fractionalKnapsack(w, arr))
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    Purpose of the Code
    The fractional knapsack problem aims to maximize profit by selecting items with the highest profit-to-weight ratio. 
    In this version, you can take fractions of items if the entire item cannot fit into the knapsack. This is different 
    from the 0/1 knapsack problem, where items are either included whole or not at all.

    Key Concepts
    Profit-to-Weight Ratio: The algorithm calculates the profit-to-weight ratio for each item and uses it to decide 
    the best items to add to the knapsack.
    Greedy Approach: It prioritizes items with the highest profit-to-weight ratio, filling the knapsack as much as 
    possible and adding fractions if necessary to maximize total profit.
    
    Code Walkthrough
    Item Class:

    Each item has a profit and a weight.
    These attributes are set when creating an Item object.
    fractionalKnapsack Function:

    Parameters:
    w:The maximum weight capacity of the knapsack.
    arr: A list of Item objects, each containing a profit and weight.
    
    Sorting Items:
    The items are sorted by their profit-to-weight ratio in descending order. This ensures that items with the 
    highest value per unit weight are considered first.
    The lambda function key=lambda x: x.profit/x.weight computes the ratio for each item.
    
    
    Filling the Knapsack:
    The function initializes finalValue to zero, which will store the total profit as items are added.
    For each item in the sorted list:
        if the item’s weight is less than or equal to the remaining knapsack capacity (w):
            -The entire item is added to the knapsack.
            -The item’s profit is added to finalValue, and its weight is subtracted from w.
        If the item’s weight is more than the remaining knapsack capacity:
            -A fraction of the item is added to fill the remaining capacity.
            -This fraction is calculated by multiplying the item’s profit by the fraction of w that the item can 
             fill (w / item.weight). 
            -Once this fraction is added, the knapsack is full, and the loop breaks.
    
    Return Value:
    The function returns finalValue, which is the maximum profit achievable given the items and knapsack capacity.

    Main Block:
    The user is prompted to enter the number of items, followed by each item’s profit and weight.
    The knapsack capacity (w) is also taken as input.
    The fractionalKnapsack function is called with the list of items and the knapsack capacity, 
    and it prints the maximum profit that can be achieved.  
    
    Suppose we have 3 items with profits and weights as follows:

Item 1: Profit = 60, Weight = 10
Item 2: Profit = 100, Weight = 20
Item 3: Profit = 120, Weight = 30
And the knapsack has a capacity of w = 50.

Steps:

1]Calculate the profit-to-weight ratio for each item:

	Item 1: 60/10 = 6
	Item 2: 100/20 = 5
	Item 3: 120/30 = 4
2]Sort items by ratio in descending order: Item 1, Item 2, Item 3.

3]Add items to the knapsack:

	Item 1 (entirely): Profit = 60, Remaining capacity = 50 - 10 = 40.
	Item 2 (entirely): Profit = 100, Remaining capacity = 40 - 20 = 20.
	Item 3 (partially, 20/30): Profit = 120 * (20/30) = 80.
4]Total Profit = 60 + 100 + 80 = 240.


Complexity Analysis
 -Time Complexity: O(nlogn) due to the sorting step, where n is the number of items.
 -Space Complexity: O(1) if we ignore input storage, as the sorting and filling operations are done in place.

Key Points for Examiner:
 -The code uses a greedy approach, prioritizing items with the highest profit-to-weight ratio.
 -It handles partial item inclusion, filling the knapsack to maximize profit.
 -Sorting items by profit-to-weight ratio is the core of the greedy method, ensuring an optimal solution for the fractional knapsack    problem.
    
    
    
    '''
    
    
    
    
    
    
    