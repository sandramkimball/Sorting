# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in arrA[i] and arrB[i]:
        if arrA[i] < arrB[i]:
            merged_arr.append(arrA[i], arrB[i])

        elif arrA[i] > arrB[i]:
            merged_arr.append(arrB[i], arrA[i])

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    for i in arr:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    # for i in range(0, n - curr_index - 1):

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
