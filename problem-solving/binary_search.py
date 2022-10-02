print("Binary Search using Python")

strr= input("Please Enter list in descending order by separating the item using black space: ")
list1= list(strr.split(" "))
# list1.sort(key=str.lower)

#print("Finding from this sorted list", list1)

find = input("Enter the value you want to check: ")

def testLocation(mid, list, key):
    
    if list[mid] == key:
        if mid-1 >= 0 and list[mid-1] == key:
            return 'left'
        else:
            return 'found'
    elif list[mid] < key:
        return 'left'
    else:
        return 'right'      

def binarySearch(list, key):
    lo, hi = 0, len(list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = testLocation(mid, list, key)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1
foundOn = binarySearch(list1, find)
if foundOn!=-1:
    print("You given input", find, "was found on", foundOn, "no position!!")
else:
    print(find, "is absent on the list!")