import time
import numpy as np
import random, sys
import matplotlib.pyplot as plt

# ***Start of Deliverable 1***

# Knapsack bottom-up dynamic programming implementation
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
    
    # check all items
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # check case for zero size or zero capacity knapsack
            if i == 0 or w == 0:
                dp[i][w] = 0
            # if there is enough room, choose whether to take the new item or not
            elif weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            # if not enough room, skip item
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Knapsack top-down with memoization dynamic programming implementation
# algorithm is from GeeksforGeeks with a few adjustments, including new variable names
def knapsack_top_down(weights, values, capacity, n):
    # initialize the matrix with -1
    memo = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]

    def knapsack(wts, val, capacity, n): 
        # base conditions
        # size zero knapsack or no capacity
        if n == 0 or capacity == 0:
            return 0
        # solution already exists
        if memo[n][capacity] != -1:
            return memo[n][capacity]

        # if enough room, chose whether to take the item or not
        if wts[n - 1] <= capacity:
            memo[n][capacity] = max(val[n - 1] + knapsack(wts, val, capacity - wts[n - 1], n - 1), knapsack(wts, val, capacity, n - 1))
            return memo[n][capacity]
        # if not enough room, skip the item
        elif wts[n - 1] > capacity:
            memo[n][capacity] = knapsack(wts, val, capacity, n - 1)
            return memo[n][capacity]

    return knapsack(weights, values, capacity, n)

# generates a random array of integers for testing
def newIntArray(n):
    ints = []
    for i in range(0, n):
        ints.append(random.randint(1,10))
    return ints

# Confirm the results of both knapsack algorithms match each other
# Runs both functions through a series of tests and returns a pass/fail result
def verificationTest(wts, vals, cap):
    print("Verification Test")
    print("Weights: ", wts)
    print("Values: ", vals)
    print("Capacity: ", cap)

    kbu = knapsack_bottom_up(wts, vals, cap)
    ktd = knapsack_top_down(wts, vals, cap, len(vals))

    try:
        assert kbu == ktd, "Failed"
        print("Passed")
        print("Bottom-Up = ", kbu)
        print("Top-Down = ", ktd)
    except AssertionError:
        print("Failed")
        print("K =",K)
        print("Bottom-Up = ", kbu)
        print("Top-Down = ", ktd)

# test knapsack algorithms and append test results to a file
with open("test.txt", "a") as file:
    sys.stdout = file # send stdout to a file
    for i in range(0,5):
        length = random.randint(0,10)
        verificationTest(newIntArray(length), newIntArray(length), random.randint(0,50))
        print()

#***End of Deliverable 1***

