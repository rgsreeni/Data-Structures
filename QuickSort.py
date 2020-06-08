def quick_sort(arr):
    quick_fn(arr,0,len(arr) -1)
def quick_fn(arr,low,high):
    if low < high:
        split = partition(arr,low,high)
        quick_fn(arr,low,split-1)
        quick_fn(arr,split+1,high)
def partition(arr,start,stop):
    pivot = arr[start]
    i = start
    j = stop
    while i < j:
        while i <= j and arr[i] <= pivot:
                i += 1
        while j >= i and arr[j] > pivot:
                j -= 1
        if i < j:
            arr[j], arr[i] = arr[i], arr[j]
    arr[start],arr[j] = arr[j],arr[start]
    return j

a = [1,5,9,8,6]
quick_sort(a)
print(a)