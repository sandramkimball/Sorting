# HELPER function to merge 2 sorted arrays:
def merge( arrA, arrB ):
    
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    for i in arrA[i] and arrB[i]:
        if arrA[i] < arrB[i]:
            merged_arr.append(arrA[i], arrB[i])

        elif arrA[i] > arrB[i]:
            merged_arr.append(arrB[i], arrA[i])

    return merged_arr


# Merge Sort function using RECURSION:
def merge_sort2( arr ):
    
    merge(arr, 0, len(arr)-1)
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

def mergee(arr, low, middle, high):
    L = arr[low:middle]
    R = arr[middle:high+1]
    L.append(999999999) #what tf is the 999999999 for???
    R.append(999999999)
    i=j=0
    for k in range (low, high+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:  
            A[k] = R[j]
            j+=1


def merge2(arr):
    merge_sort(arr, 0, len(arr)-1)

def merge_sort(arr, low, high):
    if low < high:
        middle = (low + high)//2
        merge_sort(arr, low, middle) #merge first half
        merge_sort(arr, middle+1, high) #merge second half
        merge(arr, low, middle, high) #merge all together


########



def get_pivot(arr, low, high):
    middle = (low+high)//2
    pivot = high
    if arr[low] < arr[mid]:
        pivot = middle
    elif arr[low] < arr [high]:
        pivot = low
    return pivot

#this returns array? of items sorted left or right of a pivot.
def partition(arr, low, high):
    pivotIndex = get_pivot(arr, low, high)
    pivotValue = arr[pivotIndex]
    arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]
    border = low #reference point

    for i in range(low, high+1):
        #now we move item to left of pivot if smaller
        if arr[i] < pivotValue:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    return arr[low], arr[border] = arr[border], arr[low]

def quick_sort2(arr, low, high):
    # if high - low < len(arr) and low < high:
    #     quick_selection(arr, low, high)
    if low < high:
        p = partition(arr, low, high) #this is an array?
        quick_sort2(arr, low, p-1)
        quick_sort2(arr, p+1, high)

def quick_sort(arr):
    return quick_sort2(arr, 0, len(arr)-1)