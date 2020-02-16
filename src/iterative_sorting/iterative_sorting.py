# Selection Sort: 
def selection_sort( arr ):
    for i in range(0, len(arr)):
        cur_index = i
        sml_index = cur_index #j=arr[i+1]? j=i?\
        # j = i-1
        for j in range(i, len(arr)):
            if arr[j] < arr[sml_index]:
                sml_index = j
    
        arr[sml_index], arr[cur_index] = arr[cur_index], arr[sml_index]
    return arr


# Bubble Sort:
def bubble_sort( arr ):
    n = len(arr) - 1
    while n > 0:
        n = len(arr) - 1
        for i in range(0, n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                n -= 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
