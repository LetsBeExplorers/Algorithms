import time
import numpy as np
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

#***End of Deliverable 1***

# Function to measure execution time for random inputs
def measure_execution_times(n_values, capacity_values):
    bottom_up_times = []
    top_down_times = []
    
    for n in n_values:
        weights = np.random.randint(1, max(capacity_values) // 2, n).tolist()
        values = np.random.randint(1, 100, n).tolist()
        
        bottom_up_n_times = []
        top_down_n_times = []
        
        for capacity in capacity_values:
            # Measure bottom-up execution time
            start_time = time.time()
            knapsack_bottom_up(weights, values, capacity, len(values))
            end_time = time.time()
            bottom_up_n_times.append(end_time - start_time)
            
            # Measure top-down execution time
            start_time = time.time()
            knapsack_top_down(weights, values, capacity, len(values))
            end_time = time.time()
            top_down_n_times.append(end_time - start_time)
        
        bottom_up_times.append(bottom_up_n_times)
        top_down_times.append(top_down_n_times)
    
    return bottom_up_times, top_down_times

# Plotting random input performance
def plot_random_inputs_performance(n_values, capacity_values, bottom_up_times, top_down_times):
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, n in enumerate(n_values):
        ax.plot(capacity_values, bottom_up_times[i], label=f'Bottom-Up (n={n})', linestyle='-', marker='o')
        ax.plot(capacity_values, top_down_times[i], label=f'Top-Down (n={n})', linestyle='--', marker='x')
    ax.set_xlabel('Capacity (W)')
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title('Execution Time of Knapsack Algorithms')
    ax.legend()
    plt.grid(True)
    plt.savefig('plot_random_inputs.png')
    plt.close(fig)

# Function to measure execution times for low-weight inputs
def measure_execution_times_low_weights(n_values, capacity_values):
    bottom_up_times = []
    top_down_times = []
    
    for n in n_values:
        weights = np.random.randint(1, 11, n).tolist()  # Low weights between 1 and 10
        values = np.random.randint(1, 100, n).tolist()
        
        bottom_up_n_times = []
        top_down_n_times = []
        
        for capacity in capacity_values:
            # Measure bottom-up execution time
            start_time = time.time()
            knapsack_bottom_up(weights, values, capacity, len(values))
            end_time = time.time()
            bottom_up_n_times.append(end_time - start_time)
            
            # Measure top-down execution time
            start_time = time.time()
            knapsack_top_down(weights, values, capacity, len(values))
            end_time = time.time()
            top_down_n_times.append(end_time - start_time)
        
        bottom_up_times.append(bottom_up_n_times)
        top_down_times.append(top_down_n_times)
    
    return bottom_up_times, top_down_times

# Plotting low-weight input performance
def plot_low_weight_performance(n_values, capacity_values, bottom_up_times_low, top_down_times_low):
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, n in enumerate(n_values):
        ax.plot(capacity_values, bottom_up_times_low[i], label=f'Bottom-Up Low Weights (n={n})', linestyle='-', marker='o')
        ax.plot(capacity_values, top_down_times_low[i], label=f'Top-Down Low Weights (n={n})', linestyle='--', marker='x')
    ax.set_xlabel('Capacity (W)')
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title('Execution Time of Knapsack Algorithms with Low Weights')
    ax.legend()
    plt.grid(True)
    plt.savefig('plot_low_weights.png')
    plt.close(fig)

# Function to measure execution time with varying representations of W
def measure_execution_time_representation(n, max_capacity_exponent):
    bottom_up_times = []
    top_down_times = []
    capacities = [2**exp for exp in range(1, max_capacity_exponent + 1)]
    
    weights = np.random.randint(1, 20, n).tolist()
    values = np.random.randint(1, 100, n).tolist()
    
    for capacity in capacities:
        # Measure bottom-up execution time
        start_time = time.time()
        knapsack_bottom_up(weights, values, capacity, len(values))
        end_time = time.time()
        bottom_up_times.append(end_time - start_time)
        
        # Measure top-down execution time
        start_time = time.time()
        knapsack_top_down(weights, values, capacity, len(values))
        end_time = time.time()
        top_down_times.append(end_time - start_time)
    
    return capacities, bottom_up_times, top_down_times

# Plotting pseudopolynomial-time complexity
def plot_pseudopolynomial_complexity(capacities, bottom_up_times_repr, top_down_times_repr):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(np.log2(capacities), bottom_up_times_repr, label='Bottom-Up', linestyle='-', marker='o')
    ax.plot(np.log2(capacities), top_down_times_repr, label='Top-Down', linestyle='--', marker='x')
    ax.set_xlabel('Log(Size of Representation of W)')
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title('Pseudopolynomial-Time Complexity of Knapsack Algorithms')
    ax.legend()
    plt.grid(True)
    plt.savefig('plot_pseudopolynomial.png')
    plt.close(fig)

# Test parameters
n_values = [10, 20, 30, 40, 50]
capacity_values = [50, 100, 200, 300]
n = 20  # Fixed number of items for pseudopolynomial test
max_capacity_exponent = 10  # Max exponent for 2^W in pseudopolynomial test

# Generate data and plots
bottom_up_times, top_down_times = measure_execution_times(n_values, capacity_values)
plot_random_inputs_performance(n_values, capacity_values, bottom_up_times, top_down_times)

bottom_up_times_low, top_down_times_low = measure_execution_times_low_weights(n_values, capacity_values)
plot_low_weight_performance(n_values, capacity_values, bottom_up_times_low, top_down_times_low)

capacities, bottom_up_times_repr, top_down_times_repr = measure_execution_time_representation(n, max_capacity_exponent)
plot_pseudopolynomial_complexity(capacities, bottom_up_times_repr, top_down_times_repr)
