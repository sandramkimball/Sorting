# HELPER to merge 2 sorted arrays:
def merge( arrA, arrB ):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i = 0
    j = 0

    for k in range(0, elements):
        if i >= len(arrA):
            merged_arr[k] = arrB[j]
            j += 1
        elif j >= len(arrB):
            merged_arr[k] = arrA[i]
            i +=1
        elif arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1

    return merged_arr


# Merge Sort using RECURSION:
def merge_sort( arr ):
    if len(arr) > 1:
        midpoint = int(len(arr)//2)
        left = arr[:midpoint]
        right = arr[midpoint:]

        left = merge_sort(left)
        right = merge_sort(right)

        arr = merge(left, right)
    return arr