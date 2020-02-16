# HELPER to merge 2 sorted arrays:
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    a = 0
    b = 0

    for i in range(0, elements):
        if a >= arrB[b]:
            merged_arr = arrB[b]
        elif b >= arrB[b]:
            merged_arr[i] == arrA[a]

        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrB[b]

        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

# Merge Sort using RECURSION:
def merge_sort( arr ):
    if len(arr) > 1:
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]

        l = merge_sort(left)
        r = merge_sort(right)

        arr = merge(l, r)

    return arr