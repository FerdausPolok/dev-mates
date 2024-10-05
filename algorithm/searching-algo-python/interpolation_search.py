print("Interpolation Search using Python")

input_string = input(
    "Please enter a list of sorted numbers (in ascending order) separated by spaces: "
)
list1 = list(map(int, input_string.split()))

# Handle the edge case of an empty list
if not list1:
    print("The list is empty, no search can be performed.")
    exit()

find = int(input("Enter the value you want to search for: "))


def interpolationSearch(list, key):
    lo, hi = 0, len(list) - 1

    # Handle the edge case of a single element list
    if lo == hi:
        if list[lo] == key:
            return lo
        else:
            return -1

    while lo <= hi and key >= list[lo] and key <= list[hi]:
        # If the list has identical values, return failure
        if list[hi] == list[lo]:
            if list[lo] == key:
                return lo
            else:
                return -1

        # Estimating the position using interpolation formula
        pos = lo + ((key - list[lo]) * (hi - lo)) // (list[hi] - list[lo])

        # Ensure pos is within the bounds of the list
        if pos < lo or pos > hi:
            return -1

        # Check if the estimated position holds the key
        if list[pos] == key:
            return pos

        # If the key is larger, search the right subarray
        if list[pos] < key:
            lo = pos + 1
        # If the key is smaller, search the left subarray
        else:
            hi = pos - 1

    return -1


foundOn = interpolationSearch(list1, find)

if foundOn != -1:
    print("Your given input", find, "was found at position", foundOn, "!")
else:
    print(find, "is absent in the list!")
