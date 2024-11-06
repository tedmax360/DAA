import heapq

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
    
    def __lt__(self, other):
        return self.freq < other.freq
    
def printNodes(node, val=""):
    newval = val + node.huff
    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)
    else:
        print(f"{node.symbol} -> {newval}")

#chars = ["a", "b", "c", "d", "e", "f"]
#freqs = [50, 10, 30, 5, 3, 2]
# Get input from user
chars = input("Enter the characters (e.g., a b c): ").split()
freqs = list(map(int, input("Enter the corresponding frequencies (e.g., 5 9 12): ").split()))

nodes = []

for i in range(len(chars)):
    heapq.heappush(nodes, node(freqs[i], chars[i]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = "0"
    right.huff = "1"
    newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newnode)

printNodes(nodes[0])






























































"""

The code implements Huffman coding, an algorithm used to compress data by encoding characters with variable-length binary codes. 
Characters that appear more frequently get shorter codes, while less frequent characters get longer codes, saving storage space.

1)Imports:
heapq is imported to create a min-heap or priority queue. This helps us efficiently find the two nodes with the lowest frequencies, which is key to building the Huffman tree.
Node Class:

2)The Node class represents each character and its frequency.
Each Node has:
freq: The frequency of the character.
symbol: The character itself.
left and right: Left and right children for building the tree.
huff: Holds the binary code (either "0" or "1") to be assigned based on its position in the tree.
The __lt__ method allows nodes to be compared by frequency, which is needed to prioritize nodes in the heap.

3)User Input:

The code takes two inputs from the user:
chars: A list of characters (e.g., ["a", "b", "c"]).
freqs: A list of corresponding frequencies for each character (e.g., [5, 9, 12]).
This allows the user to specify the characters and their frequencies directly.


4)Building the Initial Min-Heap:

We create a priority queue of nodes using heapq. Each character-frequency pair is pushed into nodes as a Node object.
At this point, each character is an individual node in the priority queue.

5)Building the Huffman Tree:
-The code constructs the Huffman tree by combining the two nodes with the lowest frequencies repeatedly until only one node (the root of the tree) remains.
-In each iteration:
    The two nodes with the smallest frequencies (left and right) are popped from the heap.
    We assign "0" to the left child and "1" to the right child (these will form the Huffman code).
A new node, which is the parent of left and right, is created with:
    -Frequency equal to the sum of left and right frequencies.
    -Symbol as a combination of both symbols (for internal nodes).
This new node is pushed back into the heap.
This process continues until we’re left with a single node, which is the root of the Huffman tree.

6)Generating and Printing Huffman Codes:
-The printNodes function is a recursive function that traverses the Huffman tree to print each character’s Huffman code.
-Starting from the root, the function accumulates "0" for each left traversal and "1" for each right traversal.
-When it reaches a leaf node (a node without children), it prints the character and its Huffman code.



"""



















    
