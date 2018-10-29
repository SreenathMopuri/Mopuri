# It returns location of x in given array arr If present, 
# else returns -1
def binarysearch(arr, l, r, x):
    while l <= r:
        mid = int(l + (r - l)/ 2)
        # check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
        # If x is small, ignore right half
        else:
            r = mid - 1
    # If we reach here, then the element was not present
    return -1

# Test Array
arr = [2, 4, 5, 10, 50]

x = 25

result = binarysearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
