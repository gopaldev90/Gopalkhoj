
def gopalkhoj(arr, x):
    n = len(arr)
    jump = int(n**0.5)
    prev = 0
    while arr[min(jump, n) - 1] < x:
        prev = jump
        jump += int(n**0.5)
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

if __name__ == "__main__":
    arr = [i for i in range(5678, 1000000)]
    t = 8897
    result = gopalkhoj(arr, t)
    
    print(f"Element found at index {result}" if result != -1 else "Element not found")
