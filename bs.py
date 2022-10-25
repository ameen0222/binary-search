def binarySearch(arr, l, r, x):
 
    # Check base case
  #simple step
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself any way
        if arr[mid] == x:
            return mid
 
       

        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
       #if element is return

        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
     
        return -1
 
 
#initial code steps completed 
arr = [2, 3, 4, 10, 40]
x = 10
 
# Function call poooooi
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
