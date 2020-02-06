# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  while i in range(len(arr) - 1):
    for i in arr:
      # return target in arr
      if i == target:
        return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # # TO-DO: add missing code
  counter = 0 
  while low < high:
    counter += 1
    middle = (high + low ) // 2

    if arr[middle] == target:
      return 1
      # return True
    else: 
      if target < arr[middle]:
        high = middle - 1
      else:
        low = middle + 1


  return -1 # not found
  # return False


# STRETCH: write a recursive implementation of Binary Search 
# this is where swap happens?
def binary_search_recursive(arr, target, low, high):
  pivot_index = high
  # middle = (low+high)//2

  for i in range (low, high - 1):
    if arr[pivot_index] < arr[i]:
      arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
      arr[pivot_index], arr[pivot_index + 1] = arr[pivot_index + 1], arr[pivot_index]
      pivot_index = pivot_index + 1

  # binary_search_recursive(arr, low, pivot_index - 1)
  # binary_search_recursive(arr, pivot_index + 1, pivot_index - 1)

  # TO-DO: add missing if/else statements, recursive calls
  
