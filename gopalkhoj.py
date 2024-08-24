import time
import math

# Implementations of the search algorithms

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i
    return -1

def gopalkhoj(arr, x):
    n = len(arr)
    jump = int(math.sqrt(n))
    prev = 0
    while arr[min(jump, n) - 1] < x:
        prev = jump
        jump += int(math.sqrt(n))
        if prev >= n:
            return -1
    left, right = prev, min(jump, n) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def test_search_algorithms():
    # Generate a large sorted list
    arr = list(range(1, 10000000))  # 10 million elements
    x = 9999999  # Element to search for (near the end)

    # Test Binary Search
    start_time = time.time()
    binary_result = binary_search(arr, x)
    binary_time = time.time() - start_time

    # Test Jump Search
    start_time = time.time()
    jump_result = jump_search(arr, x)
    jump_time = time.time() - start_time

    # Test Jumpnary Search
    start_time = time.time()
    jumpnary_result = gopalkhoj(arr, x)
    jumpnary_time = time.time() - start_time

    # Print Results
    print(f"Binary Search: Index {binary_result}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Index {jump_result}, Time: {jump_time:.6f} seconds")
    print(f"gopalkhoj Index {jumpnary_result}, Time: {jumpnary_time:.6f} seconds")

if __name__ == "__main__":
    test_search_algorithms()
    