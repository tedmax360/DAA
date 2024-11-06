#include <iostream>
using namespace std;

bool issafe(int** arr, int x, int y, int n){
    for(int row = 0; row<x; row++){
        if(arr[row][y] == 1){
            return false;
        }
    }

    int row = x;
    int col = y;
    
    while(row >=0 && col>=0){
        if(arr[row][col] == 1){
            return false;
        }
        row--;
        col--;
    }
    
    while(row >=0 && col<n){
        if(arr[row][col] == 1){
            return false;
        }
        row--;
        col++;
    }
    return true;
}

bool nqueen(int** arr, int x, int n){
    if(x>=n){
        return true;
    }
    
    for(int col=0; col<n; col++){
        if(issafe(arr,x,col,n)){
            arr[x][col]=1;
            
            if(nqueen(arr,x+1,n)){
                return true;
            }
            arr[x][col]=0; //backtracking
        }
    }
    return false;
}

int main() {
    int n;
    cout<<"Enter Dimensions of array: ";
    cin>>n;
    
    int** arr = new int*[n];
    
    for(int i = 0; i<n; i++){
        arr[i] = new int[n];
        for(int j = 0; j<n; j++){
            arr[i][j]=0;
        }
    }
    
    if(nqueen(arr,0,n)){
        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                cout<<arr[i][j]<<" ";
            }cout<<endl;
        }   
    }
    return 0;
}

/* 
The time complexity of the N-Queens problem can be analyzed by understanding the recursive backtracking process used to place queens on an 
𝑁×𝑁, N×N chessboard.

Overview of the Code
The code attempts to place one queen in each row while ensuring that no two queens threaten each other (i.e., no two queens are in the same column, row, or diagonal). This is done by:

Checking the current row and columns for a safe position.
Placing a queen and moving to the next row (recursive call).
Using backtracking to remove a queen if placing it in a certain position does not lead to a solution.


Recursive Complexity
Recursive Calls: For each row 𝑥, the code tries to place a queen in each column 𝑐𝑜𝑙 (from 0 to n−1).
In the worst case, for each row, there are 𝑛 possibilities, leading to a branching factor of 𝑛 n.
If 𝑥  is the current row, the function nqueen makes recursive calls for each possible column in that row.


Backtracking: If placing a queen in a certain position doesn't lead to a solution (i.e., there are no safe placements in subsequent rows), 
the code backtracks by removing the queen and trying the next column.


Time Complexity
The time complexity of the N-Queens solution is generally expressed as O(N!) for the following reasons:
    Branching Factor: In the worst case, for the first row, there are n choices. 
    For each choice in the first row, there are n−1 choices in the second row, n−2 in the third, and so on.

    Total Combinations: This results in a decreasing number of choices for each row, giving us approximately 
    n×(n−1)×(n−2)×...×1=n! total combinations to explore.

Optimizations in the Code
The issafe function reduces the number of configurations by quickly rejecting unsafe placements, but it does not change the worst-case time complexity because:
The worst-case scenario would still need to explore a significant portion of potential placements.

Final Complexity Analysis
Worst-Case Time Complexity: O(N!)
Space Complexity: 𝑂(𝑁^2), due to the N×N board used to track queen placements.
The factorial growth makes this algorithm impractical for large values of N, but it is efficient enough for reasonably small values of N, 
such as 8 in the classic 8-Queens problem.

*/
