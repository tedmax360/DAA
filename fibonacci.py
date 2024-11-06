def fibonacci_iter(n):
    if n < 0:
        return -1, 1
    if n == 0 or n == 1:
        return n, 1
    steps = 0
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
        steps += 1
    return c, steps+1

def fibonacci_recur(n):
    if n < 0:
        return -1, 1
    if n == 0 or n == 1:
        return n, 1
    fib1, steps1 = fibonacci_recur(n-1)
    fib2, steps2 = fibonacci_recur(n-2)
    return fib1 + fib2, steps1 + steps2 + 1

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print("Iterative:", fibonacci_iter(n)[0])
    print("Steps:", fibonacci_iter(n)[1])
    print("Recursive:", fibonacci_recur(n)[0])
    print("Steps:", fibonacci_recur(n)[1])
    
    
    
    
'''
1)fibonacci_iter(n):

	This function calculates the n-th Fibonacci number iteratively.
	Logic:
		Initializes a as 0 (Fibonacci[0]) and b as 1 (Fibonacci[1]).
		Uses a loop to update a and b by moving through the sequence until it reaches the n-th number.
		Tracks the number of steps (steps) taken in the process.
	Output: Returns the Fibonacci number and the number of steps.

2)fibonacci_recur(n):
	This function calculates the n-th Fibonacci number recursively.
	Logic:
		Calls itself for the n−1 th and n−2 th Fibonacci numbers.
		Tracks the number of steps by counting each recursive call.
	Output: Returns the Fibonacci number and the number of steps taken.
	
	n=5

1]iterative
Iterative Calculation (fibonacci_iter(n)):
Initial Values: a = 0, b = 1, and steps = 0.

Loop Execution:
	Iteration 1:c=a+b=0+1=1
	Update a = 1, b = 1, and increment steps = 1.

	Iteration 2:c=a+b=1+1=2
	Update a = 1, b = 2, and increment steps = 2.

	Iteration 3: c=a+b=1+2=3
	Update a = 2, b = 3, and increment steps = 3.

	Iteration 4: c=a+b=2+3=5
	Update a = 3, b = 5, and increment steps = 4.
Result:

After the loop ends, c = 5 is the 5th Fibonacci number.
Total steps is 5.


2]recusion
Base Cases:
	If n=0: return (0, 1) (Fibonacci[0] = 0, with 1 step).
	If n=1: return (1, 1) (Fibonacci[1] = 1, with 1 step).

Recursive Calls for n=5:
  fibonacci_recur(5) calls:
    fibonacci_recur(4):
      fibonacci_recur(3):
        fibonacci_recur(2):

	  fibonacci_recur(1) returns (1, 1).
          fibonacci_recur(0) returns (0, 1).
	  Sum: 1 + 0 = 1, Steps: 1 + 1 + 1 = 3.

	fibonacci_recur(1) returns (1, 1).
        Sum: 1 + 1 = 2, Steps: 3 + 1 + 1 = 5.
      fibonacci_recur(2) calls and returns (1, 3) from above.
      Sum: 2 + 1 = 3, Steps: 5 + 3 + 1 = 9.
    fibonacci_recur(3) calls and returns (2, 5) from above.
    Sum: 3 + 2 = 5, Steps: 9 + 5 + 1 = 15.
Output of Recursive: (5, 15)


Explanation of Outputs
Iterative Output: The iterative approach returns the 5th Fibonacci number 5 with 5 steps, 
as it calculates each number in sequence directly without repeated calculations.

Recursive Output: The recursive approach also finds the 5th Fibonacci number 5, but it 
takes 15 steps due to repeated calculations of the same subproblems (like fibonacci_recur(3) being called multiple times).

Summary: The iterative approach is more efficient with fewer steps, while the recursive 
approach, though correct, is less efficient for larger values of n due to repeated work.



'''
