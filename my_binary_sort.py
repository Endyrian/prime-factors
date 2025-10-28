"""
    arr: the list being searched through (assumed to be sorted)
    val: the value to search for
    returns the inex of the rightmost element of arr that is less than or equal
        to val, or -1 if there are no such elements
"""
def binary_search(arr, val):
    if len(arr) == 0 or arr[0] > val:
        return -1
    
    if len(arr) == 1:
        return 0
    
    mid = len(arr) // 2

    if val < arr[mid]:
        return binary_search(arr[:mid], val)
    else:
        return binary_search(arr[mid:], val) + mid

"""
    arr: the list being inserted into (assumed to be sorted)
    val: the value to insert
    allow_duplicates: indicates whether arr can have multiple elements with the
        same value
    inserts val into arr in place such that arr will still be sorted afterwards
"""
def binary_insert(arr, val, allow_duplicates = True):
    pos = binary_search(arr, val)

    if(allow_duplicates or pos == -1 or val != arr[pos]):
        arr.insert(pos+1, val)

"""
    arr: the list being sorted
    returs a sorted version of arr
"""
def binary_insertion_sort(arr):
    sorted_arr = []
    for val in arr:
        binary_insert(sorted_arr, val)
    return sorted_arr

if __name__ == '__main__':
    x = [int(e) for e in input('List: ').split()]
    print(binary_insertion_sort(x))
