# STRETCH: Linear Search				
def linear_search(arr, target):
  i = 0
  #often n = target
  while i in range(len(arr) - 1):
    if arr[i] == target:
      print('Found it!')
      return True
    i = i+1
  return -1   # not found


# STRETCH: Iterative Binary Search 
def binary_search(arr, target):
  low = 0
  high = len(arr)-1
  # counter = 0 do I need this??

  if len(arr) == 0:
    return -1
    
  while low <= high:
    middle = (high + low ) // 2
    middle_value = arr[middle]
    # counter += 1

    if middle_value == target:
      return True
    elif target < middle_value: 
        high = middle - 1
    else:
      low = middle + 1

  return False


# STRETCH: Recursive Binary Search 
def binary_search_recursive(arr, target, low, high):
  low = 0
  high = len(arr)-1
  middle = (low+high)//2
  
  if low > high:
    return False
  
  else:
    if target == arr[middle]:
      return True
    elif target < arr[middle]:
      return binary_search_recursive(arr, target, low, middle-1)
    else:
      return binary_search_recursive(arr, target, middle+1, high)
  
