# Selection Sort: 
def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        # j = i-1
        cur_index = arr[i]
        next_index = arr[i+1] #j=arr[i+1]? j=i?
        j = i

        while next_index > 0 and cur_index < arr[j-1]:
            if arr[j] > cur_index:
                arr[j] = next_index
            else:
                j -= 1 # cur_index -=1  
                cur_index, next_index = next_index, cur_index
               
    return arr


# Bubble Sort:
def bubble_sort( arr ):
    n = len(arr)
    for i in range(2, n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
