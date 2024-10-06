def ternary_search(arr, left, right, key):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2

        if key < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, key)
        elif key > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, key)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, key)
    
    return -1

# Example usage
arr = list(map(int, input("Enter the sorted array elements separated by spaces: ").split()))
key = int(input("Enter the key to search for: "))
result = ternary_search(arr, 0, len(arr) - 1, key)
if result != -1:
        print(f"Element found at index {result}")
else:
        print("Element not found")
