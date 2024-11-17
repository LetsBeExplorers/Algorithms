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

sys.stdout = sys.__stdout__  # Reset standard output
print("Test Results successfully written to file: test.txt")

#***End of Deliverable 1***

#***Start of Deliverable 2***

# generates a random array of integers under a given value
def newIntArrayCeiling(n, W):
    ints = []
    for i in range(0, n):
        ints.append(random.randint(1,W+1))
    return ints

# Function to measure execution time for random inputs
def test_execution_times(value, fixedW=True):
    bottom_up_times = []
    top_down_times = []
    
    if fixedW:
        capacity = value
        for n in range(1, n_top+1):
            weights = newIntArrayCeiling(n, capacity)
            values = newIntArrayCeiling(n, 25)

            # Measure execution times
            bu_time, td_time = measure_execution_times(weights, values, capacity)
            bottom_up_times.append(bu_time)
            top_down_times.append(td_time)

    # fixed n
    else: 
        n = value
        for capacity in range(50, capacity_top+1, 5):
            weights = newIntArrayCeiling(n, capacity)
            values = newIntArrayCeiling(n, 25)

            # Measure execution times
            bu_time, td_time = measure_execution_times(weights, values, capacity)
            bottom_up_times.append(bu_time)
            top_down_times.append(td_time)
    
    return bottom_up_times, top_down_times

# Function to measure execution time of both algorithms
def measure_execution_times(weights, values, capacity):
    # Measure bottom-up execution time
    start_time = time.time()
    knapsack_bottom_up(weights, values, capacity)
    end_time = time.time()
    bottom_up_time = end_time - start_time
        
    # Measure top-down execution time
    start_time = time.time()
    knapsack_top_down(weights, values, capacity, len(values))
    end_time = time.time()
    top_down_time = end_time - start_time

    return bottom_up_time, top_down_time

# Plotting random input performance for fixed W
def plot_performance_fixedW(capacity, bottom_up_times, top_down_times, smallwts=False):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(range(1, n_top+1), bottom_up_times, label=f'Bottom-Up')
    ax.plot(range(1, n_top+1), top_down_times, label=f'Top-Down')
    ax.set_xlabel('n values')
    ax.set_ylabel('Execution Time (seconds)')
    ax.legend()
    plt.grid(True)
    if not smallwts:
        ax.set_title('Execution Time of Knapsack Algorithms for Capacity = ' + str(capacity))
        plt.savefig('plot_fixedW_'+ str(capacity) + '.png')
    else:
        ax.set_title('Execution Time of Knapsack Algorithms for Capacity = ' + str(capacity) + ' and Small Weights')
        plt.savefig('plot_fixedW_'+ str(capacity) + '_smallwts.png')
    plt.close(fig)

# Plotting random input performance for fixed n
def plot_performance_fixedn(n, bottom_up_times, top_down_times,smallwts=False):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(range(50, capacity_top+1, 5), bottom_up_times, label=f'Bottom-Up')
    ax.plot(range(50, capacity_top+1, 5), top_down_times, label=f'Top-Down')
    ax.set_xlabel('capacity values')
    ax.set_ylabel('Execution Time (seconds)')
    ax.legend()
    plt.grid(True)
    if not smallwts:
        ax.set_title('Execution Time of Knapsack Algorithms for n = ' + str(n))
        plt.savefig('plot_fixedn_'+ str(n) + '.png')
    else:
        ax.set_title('Execution Time of Knapsack Algorithms for n = ' + str(n) + ' and Small Weights')
        plt.savefig('plot_fixedn_'+ str(n) + '_smallwts.png')
    plt.close(fig)

# Fixed test parameters
n_values = [10, 25, 50, 100]
capacity_values = [50, 250, 500]

# Generate data and plots for fixed W
for capacity in capacity_values:
    n_top = 100
    bottom_up_times_W, top_down_times_W = test_execution_times(capacity)
    plot_performance_fixedW(capacity, bottom_up_times_W, top_down_times_W)

print("Fixed-W timed tests successfully written to files")

# Generate data and plots for fixed n
for n in n_values:
    capacity_top = 500
    bottom_up_times_n, top_down_times_n = test_execution_times(n, False)
    plot_performance_fixedn(n, bottom_up_times_n, top_down_times_n)

print("Fixed-n timed tests successfully written to files")

#***End of Deliverable 2***

#***Start of Deliverable 3***
# Function to measure execution time for small weights
def test_execution_times_smallwts(value, fixedW=True):
    bottom_up_times = []
    top_down_times = []
    
    if fixedW:
        capacity = value
        for n in range(1, n_top+1):
            weights = newIntArrayCeiling(n, 11)
            values = newIntArrayCeiling(n, 25)

            # Measure execution times
            bu_time, td_time = measure_execution_times(weights, values, capacity)
            bottom_up_times.append(bu_time)
            top_down_times.append(td_time)

    # fixed n
    else: 
        n = value
        for capacity in range(50, capacity_top+1, 5):
            weights = newIntArrayCeiling(n, 11)
            values = newIntArrayCeiling(n, 25)

            # Measure execution times
            bu_time, td_time = measure_execution_times(weights, values, capacity)
            bottom_up_times.append(bu_time)
            top_down_times.append(td_time)
    
    return bottom_up_times, top_down_times

# Generate data and plots for fixed W - small weights
for capacity in capacity_values:
    n_top = 100
    bottom_up_times_W_smallwts, top_down_times_W_smallwts = test_execution_times(capacity)
    plot_performance_fixedW(capacity, bottom_up_times_W_smallwts, top_down_times_W_smallwts, True)

print("Fixed-W timed tests with small weights successfully written to files")

# Generate data and plots for fixed n - small weights
for n in n_values:
    capacity_top = 500
    bottom_up_times_n_smallwts, top_down_times_n_smallwts = test_execution_times(n, False)
    plot_performance_fixedn(n, bottom_up_times_n_smallwts, top_down_times_n_smallwts, True)

print("Fixed-n timed tests with small weights successfully written to files")