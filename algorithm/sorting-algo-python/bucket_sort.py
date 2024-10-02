def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Determine minimum and maximum values
    min_value = min(arr)
    max_value = max(arr)

    # Initialize buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Distribute input array values into buckets
    for i in range(len(arr)):
        index = int((arr[i] - min_value) / (max_value - min_value + 1) * bucket_count)
        buckets[index].append(arr[i])

    # Sort each bucket and concatenate the result
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array

# Example usage
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print("Original array:", arr)
    sorted_arr = bucket_sort(arr)
    print("Sorted array:", sorted_arr)