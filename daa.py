# ============================================================
# PRACTICAL 1: FIBONACCI NUMBERS USING RECURSIVE AND
#              NON-RECURSIVE METHODS
# ============================================================

import time

# ---------- Recursive Fibonacci ----------
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# ---------- Non-Recursive Fibonacci ----------
def fib_non_recursive(n):
    n1, n2 = 0, 1
    print(n1, n2, end=" ")
    for i in range(2, n):
        n3 = n1 + n2
        print(n3, end=" ")
        n1, n2 = n2, n3
    print()

# ---------- Main Function ----------
def main():
    n = int(input("Enter the number of elements: "))

    print("\nFibonacci Sequence (Recursive): ", end="")
    start1 = time.time()
    for i in range(n):
        print(fib_recursive(i), end=" ")
    end1 = time.time()
    time_recursive = (end1 - start1) * 1_000_000  # microseconds

    print("\n\nFibonacci Sequence (Non-Recursive): ", end="")
    start2 = time.time()
    fib_non_recursive(n)
    end2 = time.time()
    time_nonrecursive = (end2 - start2) * 1_000_000  # microseconds

    # ---------- Time & Space Complexity ----------
    print("\n=== Time and Space Complexity Analysis ===")
    print(f"Recursive Time Taken: {time_recursive:.2f} microseconds")
    print("Recursive Time Complexity: O(2^n)")
    print("Recursive Space Complexity: O(n)\n")

    print(f"Non-Recursive Time Taken: {time_nonrecursive:.2f} microseconds")
    print("Non-Recursive Time Complexity: O(n)")
    print("Non-Recursive Space Complexity: O(1)")

if __name__ == "__main__":
    main()


# SAMPLE OUTPUT:
#
# Enter the number of elements: 7
#
# Fibonacci Sequence (Recursive): 0 1 1 2 3 5 8
#
# Fibonacci Sequence (Non-Recursive): 0 1 1 2 3 5 8
#
# === Time and Space Complexity Analysis ===
# Recursive Time Taken: (varies) microseconds
# Recursive Time Complexity: O(2^n)
# Recursive Space Complexity: O(n)
#
# Non-Recursive Time Taken: (varies) microseconds
# Non-Recursive Time Complexity: O(n)
# Non-Recursive Space Complexity: O(1)


# ============================================================
# PRACTICAL 2: HUFFMAN ENCODING USING GREEDY ALGORITHM
# ============================================================

import heapq

# Creating Huffman tree node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq      # Frequency of symbol
        self.symbol = symbol  # Symbol name (character)
        self.left = left      # Node left of current node
        self.right = right    # Node right of current node
        self.huff = ''        # Tree direction (0/1)

    def __lt__(self, nxt):
        return self.freq < nxt.freq


# Function to print Huffman codes
def print_nodes(node, val=''):
    new_val = val + str(node.huff)
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    # If leaf node
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")


# Main function
if __name__ == "__main__":
    print("----- Huffman Coding -----")

    # Take number of symbols
    n = int(input("Enter the number of characters: "))

    chars = []
    freq = []

    # Taking input from user
    for i in range(n):
        ch = input(f"Enter character {i+1}: ")
        f = int(input(f"Enter frequency of '{ch}': "))
        chars.append(ch)
        freq.append(f)

    # Creating a list of nodes
    nodes = []
    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freq[i], chars[i]))

    # Combine nodes until one remains
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    print("\nHuffman Codes for each character:")
    print("--------------------------------")
    print_nodes(nodes[0])

# ouput:
# ----- Huffman Coding -----
# Enter the number of characters: 3
# Enter character 1: A
# Enter frequency of 'A': 5
# Enter character 2: B
# Enter frequency of 'B': 7
# Enter character 3: C
# Enter frequency of 'C': 10

# Huffman Codes for each character:
# --------------------------------
# A -> 00
# B -> 01
# C -> 1


# ============================================================
# PRACTICAL 3: FRACTIONAL KNAPSACK USING GREEDY ALGORITHM
# ============================================================

def fractional_knapsack():
    # Step 1: Take number of items
    n = int(input("Enter number of items: "))

    weights = []
    values = []

    # Step 2: Take weight and value together on same line
    print("\nEnter weight and value for each item (separated by space):")
    for i in range(n):
        w, v = map(float, input(f"Item {i+1}: ").split())
        weights.append(w)
        values.append(v)

    # Step 3: Take knapsack capacity
    capacity = float(input("\nEnter knapsack capacity: "))

    # Step 4: Fractional knapsack logic
    res = 0.0
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)

    print("\nItem selection process:")
    for weight, value in items:
        if capacity <= 0:
            break

        if weight <= capacity:
            res += value
            capacity -= weight
            print(f"  Took full item (weight={weight}, value={value})")
        else:
            res += capacity * (value / weight)
            print(f"  Took {capacity} weight fraction of item (weight={weight}, value={value})")
            capacity = 0

    print(f"\n Maximum value in knapsack = {res:.2f}")


if __name__ == "__main__":
    fractional_knapsack()

# Output:
# Enter number of items: 3
#
# Enter weight and value for each item (separated by space):
# Item 1: 10 60
# Item 2: 20 100
# Item 3: 30 120
#
# Enter knapsack capacity: 50
#
# Item selection process:
#   Took full item (weight=10.0, value=60.0)
#   Took full item (weight=20.0, value=100.0)
#   Took 20.0 weight fraction of item (weight=30.0, value=120.0)
#
#  Maximum value in knapsack = 240.00


# ============================================================
# PRACTICAL 4: 0/1 KNAPSACK USING DYNAMIC PROGRAMMING
# ============================================================

def knapsack_dp():
    # Step 1: Take user input
    n = int(input("Enter number of items: "))

    weights = []
    values = []

    print("\nEnter weight and value (profit) for each item separated by space:")
    for i in range(n):
        w, v = map(int, input(f"Item {i+1}: ").split())
        weights.append(w)
        values.append(v)

    W = int(input("\nEnter maximum capacity of knapsack: "))

    # Step 2: Create DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Step 3: Build table bottom-up
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    # Step 4: Output result
    print("\n Maximum profit that can be obtained:", dp[n][W])


if __name__ == "__main__":
    knapsack_dp()

# output:
#
# Enter number of items: 3
#
# Enter weight and value (profit) for each item separated by space:
# Item 1: 10 60
# Item 2: 20 110
# Item 3: 30 150
#
# Enter maximum capacity of knapsack: 50
#
#  Maximum profit that can be obtained: 260


# ============================================================
# PRACTICAL 5: N-QUEENS PROBLEM USING BACKTRACKING
# ============================================================

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1 or \
           (col - row + i >= 0 and board[i][col - row + i] == 1) or \
           (col + row - i < n and board[i][col + row - i] == 1):
            return False
    return True

def solve(board, row, n):
    if row == n:
        print_board(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n)
            board[row][col] = 0

def n_queens():
    n = int(input("Enter N: "))
    board = [[0]*n for _ in range(n)]
    r, c = map(int, input("Enter first queen position (row col): ").split())
    board[r-1][c-1] = 1
    print("\nInitial board:")
    print_board(board)
    print("Solutions:\n")
    solve(board, 0, n)

if __name__ == "__main__":
    n_queens()

# Output:
#
# Enter N: 4
# Enter first queen position (row col): 1 2
#
# Initial board:
# 0 1 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
#
# Solutions:
#
# Note: The code prints the boards generated by its backtracking
# function. The initially placed queen is not treated as fixed
# by the solve() function.


# ============================================================
# PRACTICAL 6: QUICK SORT USING DETERMINISTIC AND RANDOMIZED
#               PIVOT SELECTION
# ============================================================

import random

# Global step counters
det_steps = 0
rand_steps = 0

def partition(arr, low, high, steps_counter):
    steps = 0
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        steps += 1  # comparison
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps_counter[0] += steps
    return i + 1

def random_partition(arr, low, high, steps_counter):
    rand_index = random.randint(low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]  # random pivot
    return partition(arr, low, high, steps_counter)

def quick_sort_det(arr, low, high, steps_counter):
    if low < high:
        pi = partition(arr, low, high, steps_counter)
        quick_sort_det(arr, low, pi - 1, steps_counter)
        quick_sort_det(arr, pi + 1, high, steps_counter)

def quick_sort_rand(arr, low, high, steps_counter):
    if low < high:
        pi = random_partition(arr, low, high, steps_counter)
        quick_sort_rand(arr, low, pi - 1, steps_counter)
        quick_sort_rand(arr, pi + 1, high, steps_counter)

# --- Main program ---
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr1 = list(map(int, input("Enter elements: ").split()))
    arr2 = arr1.copy()

    det_counter = [0]
    rand_counter = [0]

    quick_sort_det(arr1, 0, n - 1, det_counter)
    quick_sort_rand(arr2, 0, n - 1, rand_counter)

    print("\nDeterministic QuickSort:", *arr1)
    print("Steps (approx comparisons):", det_counter[0])

    print("\nRandomized QuickSort:", *arr2)
    print("Steps (approx comparisons):", rand_counter[0])

# SAMPLE OUTPUT:
#
# Enter number of elements: 5
# Enter elements: 5 3 8 1 2
#
# Deterministic QuickSort: 1 2 3 5 8
# Steps (approx comparisons): 6
#
# Randomized QuickSort: 1 2 3 5 8
# Steps (approx comparisons): (varies)