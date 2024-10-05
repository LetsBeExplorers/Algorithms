import random
import numpy as np
import sys
import os
import requests
import re
import matplotlib.pyplot as plt

# ***Deliverable 1***

# Brute-force search algorithm
def Search(A, K):
    for i in range(len(A)):
        if A[i] == K:
            return i
    return len(A)

# generates an array of random characters
def newCharArray():
    chars = []
    upperLimit = random.randint(1,50)
    for i in range(1, upperLimit):
        chars.append(newChar())
    return chars

# generates a random characters
def newChar():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\0!@#$%^ &*().,?/\\"
    return random.choice(chars)

# wrapper for python's list.index function that returns length of array instead of -1
# when value is not found
def index(A, K):
    try:
        return A.index(K)
    except ValueError:
        return len(A)

# Confirm the results of my Search algorithm match the built in Python function
# Runs both functions through a series of tests and returns a pass/fail result
def verificationTest(A, K):
    print("Verification Test")
    print(A)

    try:
        assert Search(A, K) == index(A, K), "Failed"
        print("Passed")
        print("K =",K)
        print("Search = ", Search(A,K))
        print("Index = ", index(A, K))
    except AssertionError:
        print("Failed")
        print("K =",K)
        print("Search = ", Search(A,K))
        print("Index = ", index(A, K))

# test search algorithm against python search alogrithm
# append test results to a file

with open("test.txt", "a") as file:
    sys.stdout = file # send stdout to a file
    for i in range(0,5):
        verificationTest(newCharArray(), newChar())
        print()

sys.stdout = sys.__stdout__  # Reset standard output
print("Test Results successfully written to file: test.txt")

# ***End of Deliverable 1***

# ***Deliverable 2***

# Function to download text from Project Gutenberg
def download_text(url):
    response = requests.get(url)
    text = response.text

    # Remove headers/footers from the text (Project Gutenberg specific cleaning)
    start_index = re.search(r"\*\*\* START OF THE PROJECT GUTENBERG EBOOK FOLK TALES EVERY CHILD SHOULD KNOW", text)
    end_index = re.search(r"\*\*\* END OF THE PROJECT GUTENBERG EBOOK FOLK TALES EVERY CHILD SHOULD KNOW", text)
    
    if start_index and end_index:
        text = text[start_index.end():end_index.start()]

    # Remove carriage returns and new lines
    text = text.replace('\r', '')
    text = text.replace('\n', '')
    
    print("Book Successfully downloaded from Project Gutenberg and written to file: english_text.txt")
    return text

# Function to generate character arrays from text
def generate_datasets(text, sizes, num_arrays):
    datasets = {}
    text_length = len(text)
    start = 0 
    for n in sizes:
        datasets[n] = []
        for i in range(num_arrays):
            datasets[n].append(list(text[start:start+n]))
            start += n+1
    return datasets

# Download and clean text from Project Gutenberg
gutenberg_url = "https://www.gutenberg.org/cache/epub/15164/pg15164.txt"  # Folk Tales Every Child Should Know by Hamilton Wright Mabie
text = download_text(gutenberg_url)

# Save the downloaded text to a file
with open("english_text.txt", "w") as file:
    file.write(text)

# Dataset sizes
sizes = [100, 175, 250, 325, 400, 475, 550, 625, 700, 775]
num_arrays_per_size = 50

# Generate datasets
datasets = generate_datasets(text, sizes, num_arrays_per_size)

# check if output file already exists. If so, delete it
datasetsFile = 'datasets.txt'
if os.path.exists(datasetsFile):
    os.remove(datasetsFile)
    print("Reset datasets output file.")

with open(datasetsFile, "a") as file:
    sys.stdout = file # send stdout to a file
    [print(f"{key}: {value}") for key, value in datasets.items()]

sys.stdout = sys.__stdout__  # Reset standard output
print("Datasets succesfully written to file: datasets.txt")

# *** End of Deliverable 2 ***

# *** Start of Deliverables 3, 4, 5 ***

# Function to run experiments and record runtimes
def run_experiments(datasets, characters):
    results = {char: {'worst': [], 'best': [], 'average': []} for char in characters}

    for char in characters:
        for n, arrays in datasets.items():
            times = []
            for A in arrays:
                times.append(Search(A, char))

            # Record the best, worst, and average runtime
            results[char]['worst'].append(max(times))
            results[char]['best'].append(min(times))
            results[char]['average'].append(sum(times) / len(times))

    return results

# Run experiments
test_characters = ['e', 'm', 'Q', '%']
results = run_experiments(datasets, test_characters)

resultsFile = 'results.txt'
if os.path.exists(resultsFile):
    os.remove(resultsFile)
    print("Reset results output file.")

with open(resultsFile, "a") as file:
    sys.stdout = file # send stdout to a file
    [print(f"{key}: {value}") for key, value in results.items()]

sys.stdout = sys.__stdout__  # Reset standard output
print("Experiment results succesfully written to file: results.txt")

# Plotting function for all character results on one graph
def plot_results(results, sizes, output_name):
    for char, data in results.items():
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, data['worst'], label='Worst case', marker='o')
        plt.plot(sizes, data['best'], label='Best case', marker='o')
        plt.plot(sizes, data['average'], label='Average case', marker='o')
        plt.title(f"Runtime analysis for character: {char}")
        plt.xlabel("Array Size (n)")
        plt.ylabel("Runtime")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{output_name}_{char}.pdf")  # Save plot for LaTeX
        plt.close()

# Plotting function
def plot_result(results, sizes, output_name, case, case_label):
    for char, data in results.items():
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, data[case], label=case_label, marker='o')
        plt.title(f"{case}-case runtime analysis for character: {char}")
        plt.xlabel("Array Size (n)")
        plt.ylabel("Runtime")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{output_name}_{char}.pdf")  # Save plot for LaTeX
        plt.close()

# filters a dictionary by key
def filterByKey(x, data):
    return lambda keys: {x: data[x] for x in keys}

# determine how to plot results based on key value
for key in results.keys():
    if (key == 'e'):
        newDict = {key: results[key] for key in results.keys() & 'e'}
        plot_results(newDict, sizes, "runtime_analysis")
    elif (key == 'm'):
        newDict = {key: results[key] for key in results.keys() & 'm'}
        plot_results(newDict, sizes, "runtime_analysis")
    elif (key == 'Q'):
        newDict = {key: results[key] for key in results.keys() & 'Q'}
        plot_result(newDict, sizes, "runtime_analysis_best", 'best', 'Best Case')
        plot_result(newDict, sizes, "runtime_analysis_worst", 'worst', 'Worst Case')
        plot_result(newDict, sizes, "runtime_analysis_average", 'average', 'Average Case')
    elif (key == '%'):
        newDict = {key: results[key] for key in results.keys() & '%'}
        plot_result(newDict, sizes, "runtime_analysis_best", 'best', 'Best Case')
        plot_result(newDict, sizes, "runtime_analysis_worst", 'worst', 'Worst Case')
        plot_result(newDict, sizes, "runtime_analysis_average", 'average', 'Average Case')

print("Results successfully graphed and saved to files")

# *** End of Deliverables 3, 4, 5 ***
