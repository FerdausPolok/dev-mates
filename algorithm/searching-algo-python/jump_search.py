def manual_sqrt(n):
    # Babylonian method
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def jump_search(arr, target):
    n = len(arr)
    step = manual_sqrt(n)  # Using the manual square root calculation
    
    # Jump through the array
    for i in range(0, n, step):
        # If we find a block that may contain the target
        if arr[min(i + step, n) - 1] >= target:
            # Applying Linear search within the block to find the index 
            for j in range(i, min(i + step, n)):
                if arr[j] == target:
                    return j
            break
    return -1

# Taking user input for the array
arr = list(map(int, input("Enter elements of the array separated by spaces: ").split()))
target = int(input("Enter the target element: "))

result = jump_search(arr, target)
print("Element found at index:", result if result != -1 else "Element not found")
