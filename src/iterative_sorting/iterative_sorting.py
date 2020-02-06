# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        next_index = [cur_index + 1]
        while smallest_index < next_index:
            # find next smallest element (hint, can do in 3 loc)  
            # swap nums if needed
            if cur_index > next_index:
                smallest_index = next_index
            else:
                cur_index = next_index

    return arr


# implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(2, len(arr) - 1):
        curr_index = i

        for j in range(0, n - curr_index - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr_index = arr[i]
        j = i
        while j > 0 and curr_index < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = curr_index
    return arr