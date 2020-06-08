def binary_search(arr,target):
    mn = 0
    mx = len(arr) - 1
    found = False
    while mn <= mx and not found:
        mid = (mn + mx) // 2
        if arr[mid] == target:
            found = True
        else:
            if arr[mid] < target:
                mn = mid + 1
            else:
                mx = mid - 1
    return found

#using recursion

def bins_recur(arr,target):
    if len(arr) == 0:
        return False
    mid = (len(arr) -1) //2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return bins_recur(arr[mid + 1:],target)
    else:
        return bins_recur(arr[:mid - 1], target)