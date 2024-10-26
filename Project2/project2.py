import random
import time
import sys
import matplotlib.pyplot as plt

# ***Start of Deliverable 1***

# Insertion sort implementation
def insertion_sort(arr):
    n = len(arr)

    # if the array has 0 or 1 items then it is already sorted
    if n <= 1:
        return arr

    for i in range(1, n):
        # current item is the key to be inserted in the right position
        key = arr[i]
        j = i - 1

        # move items greater than key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # shift items to the right
            j -= 1

        # put the key in the right position
        arr[j + 1] = key

    return arr

# Merge function for merge sort
def merge(left, right):
    result = []
    i = j = 0

    # compare the items of both arrays and append whichever is smaller
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]) # left item was smaller so add it
            i += 1
        else:
            result.append(right[j]) # right item was smaller so add it
            j += 1

    # if left was emptied first, then add the rest of the right array
    if i == len(left):
        result.extend(right[j:])
    else: # otherwise add the rest of the left array
        result.extend(left[i:])
    
    return result

# Hybrid sort implementation
def hybrid_sort(arr, K):
    # for values that are at or below the threshold, use insertion sort
    if len(arr) <= K:
        return insertion_sort(arr)
    else: # otherwise recursively sort the array using mergesort techniques
        mid = len(arr) // 2
        left = hybrid_sort(arr[:mid], K)
        right = hybrid_sort(arr[mid:], K)
        return merge(left, right)

# generates a random array of integers (random length) for sorting
def newIntArray():
    ints = []
    upperLimit = random.randint(10,50)
    for i in range(1, upperLimit):
        ints.append(random.randint(0,100))
    return ints

# Confirm the results of my Search algorithm match the built in Python function
# Runs both functions through a series of tests and returns a pass/fail result
def verificationTest(A, K):
    print("Verification Test")
    print(A)

    try:
        assert hybrid_sort(A, K) == sorted(A), "Failed"
        print("Passed")
        print("K =",K)
        print("Hybrid = ", hybrid_sort(A,K))
        print("Sort = ", sorted(A))
    except AssertionError:
        print("Failed")
        print("K =",K)
        print("Hybrid = ", hybrid_sort(A,K))
        print("Sort = ", sorted(A))

# test sorting algorithm against python sorting alogrithm
# append test results to a file

with open("test.txt", "a") as file:
    sys.stdout = file # send stdout to a file
    for i in range(0,5):
        verificationTest(newIntArray(), 5) # set K to 5 for testing
        print()

sys.stdout = sys.__stdout__  # Reset standard output
print("Test Results successfully written to file: test.txt")

# ***End of Deliverable 1***

# Function to run time experiments
def run_time_experiment(K_values, n_values, num_trials=5, sorted_input=False):
    avg_times = {n: [] for n in n_values}
    for n in n_values:
        for K in K_values:
            total_time = 0
            for _ in range(num_trials):
                if sorted_input:
                    arr = sorted(random.sample(range(1000000), n))
                else:
                    arr = random.sample(range(1000000), n)
                start_time = time.time()
                hybrid_sort(arr, K)
                total_time += time.time() - start_time
            avg_times[n].append(total_time / num_trials)
    return avg_times

# Finding optimal K for different n values
def find_optimal_k(avg_times, K_values, n_values):
    optimal_ks = []
    for n in n_values:
        min_time = min(avg_times[n])
        optimal_k = K_values[avg_times[n].index(min_time)]
        optimal_ks.append(optimal_k)
    return optimal_ks

# Plotting functions
def plot_results(avg_times, K_values, n_values, filename, title):
    for n in n_values:
        plt.plot(K_values, avg_times[n], label=f"n={n}")
    plt.xlabel("K")
    plt.ylabel("Average Running Time (seconds)")
    plt.title(title)
    plt.legend()
    plt.savefig(filename)
    plt.close()

def plot_optimal_k(optimal_ks, n_values, filename):
    plt.plot(n_values, optimal_ks, marker='o')
    plt.xlabel("Array Size (n)")
    plt.ylabel("Optimal K")
    plt.title("Optimal K as a Function of Array Length")
    plt.savefig(filename)
    plt.close()

# Example experiment settings
#K_values = list(range(2, 51, 5))  # K from 2 to 50 with step 5
#n_values = [1000, 5000, 10000, 20000]  # Array lengths

# 1. Run experiments on random arrays
#avg_times_random = run_time_experiment(K_values, n_values)

# Save the plot for random array results
#plot_results(avg_times_random, K_values, n_values, "random_results.png", "Average Running Time on Random Arrays")

# 2. Identify optimal K for each n on random arrays
#optimal_ks_random = find_optimal_k(avg_times_random, K_values, n_values)

# Save the plot for optimal K on random arrays
#plot_optimal_k(optimal_ks_random, n_values, "optimal_k.png")

# 3. Run experiments on sorted arrays
#avg_times_sorted = run_time_experiment(K_values, n_values, sorted_input=True)

# Save the plot for sorted array results
#plot_results(avg_times_sorted, K_values, n_values, "sorted_results.png", "Average Running Time on Sorted Arrays")

# 4. Identify optimal K for sorted arrays
#optimal_ks_sorted = find_optimal_k(avg_times_sorted, K_values, n_values)

# Save the plot for optimal K on sorted arrays
#plot_optimal_k(optimal_ks_sorted, n_values, "optimal_k_sorted.png")
