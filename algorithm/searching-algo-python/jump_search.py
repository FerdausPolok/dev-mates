import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    
    # Jump through the array with a for loop
    for i in range(0, n, step):
        # If we find a block that may contain the target
        if arr[min(i + step, n) - 1] >= target:
            # Applying Linear search within the block to find the index 
            for j in range(i, min(i + step, n)):
                if arr[j] == target:
                    return j
            break
    return -1

# Example usage
arr = [1,20,300,4000,5000]
target = 20
result = jump_search(arr, target)
print("Element found at index:", result if result != -1 else "Element not found")
