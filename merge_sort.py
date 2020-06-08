def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = (len(arr)) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge_fn(merge_sort(left),merge_sort(right))
def merge_fn(a,b):
    out = []
    i , j = 0,0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    while i < len(a):
        out.append(a[i])
        i += 1
    while j < len(b):
        out.append(b[j])
        j += 1
    return out