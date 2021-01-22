def bin_search(key, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        m = left + (right - left) // 2
        if arr[m] == key:
            return m + 1
        elif arr[m] > key:
            right = m - 1
        elif arr[m] < key:
            left = m + 1
    return -1
